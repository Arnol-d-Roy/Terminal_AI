#!/bin/bash
# Universal launcher for Claude Code Tutorial
# Works with both python and python3

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Try python first, then python3
if command -v python &> /dev/null; then
    python claude-tutorial.py
elif command -v python3 &> /dev/null; then
    python3 claude-tutorial.py
else
    echo "Error: Python not found!"
    echo "Please install Python 3:"
    echo "  sudo apt update"
    echo "  sudo apt install python3"
    exit 1
fi
