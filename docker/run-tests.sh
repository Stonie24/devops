#!/bin/sh
set -e

echo "Running tests..."
cd /app
make test
