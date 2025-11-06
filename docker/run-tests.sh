#!/bin/bash
set -e

echo "Running tests..."
# Ensure we're in the folder with Makefile
cd /app

# Run tests
make test
