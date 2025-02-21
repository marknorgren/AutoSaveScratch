# List available commands
default:
    @just --list

# Create and activate virtual environment
venv:
    python3.11 -m venv .venv
    . .venv/bin/activate
    python -m pip install --upgrade pip

# Install development dependencies
setup: venv
    . .venv/bin/activate && python -m pip install black ruff pytest
    . .venv/bin/activate && python -m pip install -e .

# Format code with black
format:
    . .venv/bin/activate && black .

# Check formatting without making changes
format-check:
    . .venv/bin/activate && black --check .

# Run ruff linter
lint:
    . .venv/bin/activate && ruff check .

# Run ruff with auto-fix
lint-fix:
    . .venv/bin/activate && ruff check --fix .

# Run all checks (format and lint)
check: format-check lint

# Run all checks and fix issues
fix: format lint-fix

# Clean up python cache files
clean:
    find . -type d -name "__pycache__" -exec rm -r {} +
    find . -type f -name "*.pyc" -delete
    find . -type f -name "*.pyo" -delete
    find . -type f -name "*.pyd" -delete
    find . -type d -name "*.egg-info" -exec rm -r {} +
    find . -type d -name "*.egg" -exec rm -r {} +
    find . -type d -name ".pytest_cache" -exec rm -r {} +
    find . -type d -name ".ruff_cache" -exec rm -r {} +

# Install the plugin in Sublime Text
install:
    . .venv/bin/activate && python scripts/autosave_sublime_setup.py

# Uninstall the plugin from Sublime Text
uninstall:
    . .venv/bin/activate && python -c "import os, sys; p = os.path.expanduser('~/Library/Application Support/Sublime Text/Packages/User'); [os.remove(os.path.join(p, f)) for f in ['auto_save_new_files.py', 'AutoSaveNewFiles.sublime-settings'] if os.path.exists(os.path.join(p, f))]"

# Run a complete test cycle (clean, check, install)
test: clean check install

# Create a new development branch
branch NAME:
    git checkout -b {{NAME}}

# Update all development dependencies
update-deps:
    . .venv/bin/activate && python -m pip install --upgrade black ruff pytest

# Remove virtual environment and clean
reset: clean
    rm -rf .venv

# Show current environment info
info:
    . .venv/bin/activate && python --version
    . .venv/bin/activate && pip list

# Run format and lint checks
check-all: format-check lint 