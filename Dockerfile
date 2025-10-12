# Dockerfile for Clarion Knowledge Base MCP Server
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies (skip pywin32 - Windows-only)
RUN grep -v "pywin32" requirements.txt > requirements-docker.txt && \
    pip install --no-cache-dir -r requirements-docker.txt && \
    rm requirements-docker.txt

# Copy source code
COPY src/ ./src/

# Copy documentation (optional, for reference)
COPY documentation/ ./documentation/

# Create data directory structure
RUN mkdir -p /app/data/processed

# Set Python to use UTF-8 encoding
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=utf-8

# The MCP server will be run via docker exec, not as an entry point
# This allows Claude Code/Desktop to execute it on-demand via stdio
# Default command keeps container running
CMD ["tail", "-f", "/dev/null"]
