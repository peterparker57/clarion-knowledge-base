"""
Import Qdrant Vector Database Snapshot

This script imports a compressed Qdrant snapshot into a running Qdrant instance.
Used during installation to load the pre-built vector database.

The script:
1. Extracts the snapshot from tar.gz
2. Uploads it to Qdrant via REST API
3. Recovers the collection from the snapshot
4. Cleans up temporary files

Usage:
    python scripts/import_snapshot.py [snapshot_file]

Arguments:
    snapshot_file: Path to qdrant-snapshot.tar.gz (default: ./qdrant-snapshot.tar.gz)

Requirements:
    - Qdrant must be running (localhost:6333)
    - Docker containers must be started
"""

import requests
import time
import sys
import os
from pathlib import Path
import tarfile
import shutil

# Configuration
QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "clarion_docs"
DEFAULT_SNAPSHOT_FILE = "qdrant-snapshot.tar.gz"

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')


def log(message):
    """Print log message with timestamp."""
    print(f"[{time.strftime('%H:%M:%S')}] {message}")


def check_qdrant_running():
    """Check if Qdrant is accessible."""
    log("Checking if Qdrant is accessible...")
    try:
        response = requests.get(f"{QDRANT_URL}/health", timeout=5)
        response.raise_for_status()
        log("✓ Qdrant is running and accessible")
        return True
    except Exception as e:
        log(f"✗ Cannot access Qdrant: {e}")
        return False


def extract_snapshot(snapshot_file, temp_dir):
    """Extract snapshot from tar.gz file."""
    log(f"Extracting snapshot from {snapshot_file}...")

    if not os.path.exists(snapshot_file):
        log(f"✗ Snapshot file not found: {snapshot_file}")
        return None

    try:
        os.makedirs(temp_dir, exist_ok=True)

        with tarfile.open(snapshot_file, "r:gz") as tar:
            tar.extractall(temp_dir)

        # Find the extracted snapshot file
        snapshot_files = [f for f in os.listdir(temp_dir) if f.endswith('.snapshot')]
        if not snapshot_files:
            log("✗ No .snapshot file found in archive")
            return None

        snapshot_path = os.path.join(temp_dir, snapshot_files[0])
        size_mb = os.path.getsize(snapshot_path) / (1024 * 1024)
        log(f"✓ Snapshot extracted to {snapshot_path} ({size_mb:.2f} MB)")
        return snapshot_path

    except Exception as e:
        log(f"✗ Error extracting snapshot: {e}")
        return None


def upload_snapshot(snapshot_path):
    """Upload snapshot to Qdrant."""
    log("Uploading snapshot to Qdrant...")

    try:
        with open(snapshot_path, 'rb') as f:
            files = {'snapshot': f}
            response = requests.post(
                f"{QDRANT_URL}/collections/{COLLECTION_NAME}/snapshots/upload",
                files=files,
                timeout=300  # 5 minutes timeout for large files
            )
            response.raise_for_status()

        log("✓ Snapshot uploaded successfully")
        return True

    except Exception as e:
        log(f"✗ Error uploading snapshot: {e}")
        return False


def recover_collection(snapshot_name):
    """Recover collection from snapshot."""
    log(f"Recovering collection from snapshot...")

    try:
        # Delete existing collection if it exists
        try:
            response = requests.delete(f"{QDRANT_URL}/collections/{COLLECTION_NAME}")
            log("✓ Deleted existing collection")
        except:
            log("  No existing collection to delete")

        # Recover from snapshot
        payload = {
            "location": f"file:///qdrant/storage/snapshots/{COLLECTION_NAME}/{snapshot_name}"
        }
        response = requests.put(
            f"{QDRANT_URL}/collections/{COLLECTION_NAME}/snapshots/{snapshot_name}/recover",
            json=payload
        )
        response.raise_for_status()

        log("✓ Collection recovered from snapshot")
        return True

    except Exception as e:
        log(f"✗ Error recovering collection: {e}")
        return False


def verify_collection():
    """Verify the collection was imported correctly."""
    log("Verifying collection...")

    try:
        response = requests.get(f"{QDRANT_URL}/collections/{COLLECTION_NAME}")
        response.raise_for_status()
        data = response.json()

        result = data.get('result', {})
        points_count = result.get('points_count', 0)
        vectors_count = result.get('vectors_count', 0)

        log(f"✓ Collection verified:")
        log(f"  Name: {COLLECTION_NAME}")
        log(f"  Points: {points_count:,}")
        log(f"  Vectors: {vectors_count:,}")

        if points_count == 0:
            log("⚠ Warning: Collection is empty")
            return False

        return True

    except Exception as e:
        log(f"✗ Error verifying collection: {e}")
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
    """Main import process."""
    log("=" * 60)
    log("Qdrant Snapshot Import Utility")
    log("=" * 60)

    # Get snapshot file path
    if len(sys.argv) > 1:
        snapshot_file = sys.argv[1]
    else:
        snapshot_file = DEFAULT_SNAPSHOT_FILE

    snapshot_file = os.path.abspath(snapshot_file)
    log(f"Snapshot file: {snapshot_file}")

    if not os.path.exists(snapshot_file):
        log(f"\n✗ FAILED: Snapshot file not found: {snapshot_file}")
        sys.exit(1)

    # Step 1: Check Qdrant is running
    if not check_qdrant_running():
        log("\n✗ FAILED: Qdrant is not accessible")
        log("  Please ensure Docker containers are running:")
        log("  docker-compose up -d")
        sys.exit(1)

    # Step 2: Extract snapshot
    temp_dir = "temp_import"
    snapshot_path = extract_snapshot(snapshot_file, temp_dir)
    if not snapshot_path:
        log("\n✗ FAILED: Could not extract snapshot")
        cleanup_temp_files(temp_dir)
        sys.exit(1)

    snapshot_name = os.path.basename(snapshot_path)

    # Step 3: Upload snapshot
    if not upload_snapshot(snapshot_path):
        log("\n✗ FAILED: Could not upload snapshot")
        cleanup_temp_files(temp_dir)
        sys.exit(1)

    # Give Qdrant a moment to process
    log("Waiting for Qdrant to process snapshot...")
    time.sleep(2)

    # Step 4: Recover collection
    if not recover_collection(snapshot_name):
        log("\n✗ FAILED: Could not recover collection")
        cleanup_temp_files(temp_dir)
        sys.exit(1)

    # Give Qdrant a moment to recover
    log("Waiting for collection recovery...")
    time.sleep(3)

    # Step 5: Verify collection
    if not verify_collection():
        log("\n✗ FAILED: Collection verification failed")
        cleanup_temp_files(temp_dir)
        sys.exit(1)

    # Step 6: Cleanup
    cleanup_temp_files(temp_dir)

    # Success!
    log("=" * 60)
    log("✓ SUCCESS: Snapshot imported successfully!")
    log("=" * 60)
    log(f"Collection '{COLLECTION_NAME}' is ready to use")
    log("")
    log("Next steps:")
    log("  1. Configure Claude Code or Claude Desktop")
    log("  2. Restart Claude application")
    log("  3. Test the MCP server connection")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("\n\n✗ Import cancelled by user")
        sys.exit(1)
    except Exception as e:
        log(f"\n✗ FATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
