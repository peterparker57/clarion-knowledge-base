"""
Export Qdrant Vector Database Snapshot

This script creates a compressed snapshot of the Qdrant vector database
from the Docker container for distribution via GitHub Release.

The script:
1. Creates a snapshot using Qdrant's snapshot API
2. Copies the snapshot from the Docker container
3. Compresses it into a tar.gz file
4. Cleans up temporary files

Usage:
    python scripts/export_snapshot.py

Output:
    qdrant-snapshot.tar.gz (in project root)
"""

import requests
import subprocess
import time
import sys
import os
from pathlib import Path
import tarfile
import shutil

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Configuration
QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "clarion_docs"
CONTAINER_NAME = "qdrant_clarion"
OUTPUT_FILE = "qdrant-snapshot.tar.gz"


def log(message):
    """Print log message with timestamp."""
    print(f"[{time.strftime('%H:%M:%S')}] {message}")


def check_qdrant_running():
    """Check if Qdrant container is running."""
    log("Checking if Qdrant is running...")
    try:
        result = subprocess.run(
            ["docker", "ps", "--filter", f"name={CONTAINER_NAME}", "--format", "{{.Names}}"],
            capture_output=True,
            text=True,
            check=True
        )
        if CONTAINER_NAME in result.stdout:
            log(f"✓ Qdrant container '{CONTAINER_NAME}' is running")
            return True
        else:
            log(f"✗ Qdrant container '{CONTAINER_NAME}' is not running")
            return False
    except subprocess.CalledProcessError as e:
        log(f"✗ Error checking container status: {e}")
        return False


def get_collection_info():
    """Get information about the collection."""
    log(f"Getting collection info for '{COLLECTION_NAME}'...")
    try:
        response = requests.get(f"{QDRANT_URL}/collections/{COLLECTION_NAME}")
        response.raise_for_status()
        data = response.json()

        result = data.get('result', {})
        points_count = result.get('points_count', 0)
        vectors_count = result.get('vectors_count', 0)

        log(f"✓ Collection: {COLLECTION_NAME}")
        log(f"  Points: {points_count:,}")
        log(f"  Vectors: {vectors_count:,}")

        return points_count, vectors_count
    except Exception as e:
        log(f"✗ Error getting collection info: {e}")
        return None, None


def create_snapshot():
    """Create a snapshot using Qdrant API."""
    log(f"Creating snapshot for collection '{COLLECTION_NAME}'...")
    try:
        response = requests.post(f"{QDRANT_URL}/collections/{COLLECTION_NAME}/snapshots")
        response.raise_for_status()
        data = response.json()

        snapshot_name = data.get('result', {}).get('name')
        if snapshot_name:
            log(f"✓ Snapshot created: {snapshot_name}")
            return snapshot_name
        else:
            log("✗ No snapshot name returned")
            return None
    except Exception as e:
        log(f"✗ Error creating snapshot: {e}")
        return None


def download_snapshot(snapshot_name, temp_dir):
    """Download snapshot from Qdrant via HTTP API."""
    log("Downloading snapshot from Qdrant...")

    local_path = os.path.join(temp_dir, snapshot_name)
    download_url = f"{QDRANT_URL}/collections/{COLLECTION_NAME}/snapshots/{snapshot_name}"

    try:
        # Download snapshot via HTTP
        response = requests.get(download_url, stream=True)
        response.raise_for_status()

        # Write to file in chunks
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        if os.path.exists(local_path):
            size_mb = os.path.getsize(local_path) / (1024 * 1024)
            log(f"✓ Snapshot downloaded to {local_path} ({size_mb:.2f} MB)")
            return local_path
        else:
            log(f"✗ Snapshot file not found after download: {local_path}")
            return None
    except Exception as e:
        log(f"✗ Error downloading snapshot: {e}")
        return None


def compress_snapshot(snapshot_path, output_file):
    """Compress snapshot into tar.gz file."""
    log(f"Compressing snapshot to {output_file}...")
    try:
        with tarfile.open(output_file, "w:gz") as tar:
            tar.add(snapshot_path, arcname=os.path.basename(snapshot_path))

        if os.path.exists(output_file):
            size_mb = os.path.getsize(output_file) / (1024 * 1024)
            log(f"✓ Compressed snapshot created: {output_file} ({size_mb:.2f} MB)")
            return True
        else:
            log(f"✗ Failed to create compressed file")
            return False
    except Exception as e:
        log(f"✗ Error compressing snapshot: {e}")
        return False


def cleanup_temp_files(temp_dir):
    """Clean up temporary directory."""
    log("Cleaning up temporary files...")
    try:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            log("✓ Temporary files cleaned up")
    except Exception as e:
        log(f"⚠ Warning: Could not clean up temp files: {e}")


def main():
    """Main export process."""
    log("=" * 60)
    log("Qdrant Snapshot Export Utility")
    log("=" * 60)

    # Change to project root
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)
    log(f"Working directory: {project_root}")

    # Step 1: Check Qdrant is running
    if not check_qdrant_running():
        log("\n✗ FAILED: Qdrant container is not running")
        log("  Please start Qdrant with: docker start qdrant_clarion")
        sys.exit(1)

    # Step 2: Get collection info
    points_count, vectors_count = get_collection_info()
    if points_count is None:
        log("\n✗ FAILED: Could not access collection")
        sys.exit(1)

    if points_count == 0:
        log("\n✗ FAILED: Collection is empty")
        sys.exit(1)

    # Step 3: Create snapshot
    snapshot_name = create_snapshot()
    if not snapshot_name:
        log("\n✗ FAILED: Could not create snapshot")
        sys.exit(1)

    # Wait a moment for snapshot to be written
    log("Waiting for snapshot to be written...")
    time.sleep(2)

    # Step 4: Download snapshot
    temp_dir = "temp_snapshot"
    os.makedirs(temp_dir, exist_ok=True)

    snapshot_path = download_snapshot(snapshot_name, temp_dir)
    if not snapshot_path:
        log("\n✗ FAILED: Could not download snapshot")
        cleanup_temp_files(temp_dir)
        sys.exit(1)

    # Step 5: Compress snapshot
    output_path = os.path.join(project_root, OUTPUT_FILE)
    if os.path.exists(output_path):
        log(f"⚠ Warning: {OUTPUT_FILE} already exists, it will be overwritten")
        os.remove(output_path)

    if not compress_snapshot(snapshot_path, output_path):
        log("\n✗ FAILED: Could not compress snapshot")
        cleanup_temp_files(temp_dir)
        sys.exit(1)

    # Step 6: Cleanup
    cleanup_temp_files(temp_dir)

    # Success!
    log("=" * 60)
    log("✓ SUCCESS: Snapshot exported successfully!")
    log("=" * 60)
    log(f"Output file: {output_path}")

    final_size_mb = os.path.getsize(output_path) / (1024 * 1024)
    log(f"File size: {final_size_mb:.2f} MB")
    log(f"Collection: {COLLECTION_NAME}")
    log(f"Points: {points_count:,}")
    log(f"Vectors: {vectors_count:,}")
    log("")
    log("This file is ready to be uploaded as a GitHub Release asset.")
    log("Users will download this file during installation.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("\n\n✗ Export cancelled by user")
        sys.exit(1)
    except Exception as e:
        log(f"\n✗ FATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
