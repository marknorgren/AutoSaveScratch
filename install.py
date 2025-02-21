#!/usr/bin/env python3
"""
Installation script for AutoSaveNewFiles Sublime Text Plugin.
This script will:
1. Detect the Sublime Text Packages directory
2. Create necessary directories
3. Copy plugin files
4. Create default configuration
"""

import json
import os
import shutil
import sys
from pathlib import Path


def get_sublime_packages_dir():
    """Get the Sublime Text Packages directory based on the OS."""
    home = str(Path.home())

    if sys.platform == "darwin":  # macOS
        return os.path.join(home, "Library", "Application Support", "Sublime Text", "Packages")
    elif sys.platform == "win32":  # Windows
        return os.path.join(os.getenv("APPDATA"), "Sublime Text", "Packages")
    else:  # Linux
        return os.path.join(home, ".config", "sublime-text", "Packages")


def create_default_config():
    """Create default configuration dictionary."""
    return {
        "save_directory": "~/scratch",
        "filename_format": "{timestamp}.{extension}",
        "insert_timestamp": True,
        "timestamp_format": "%Y_%m_%d_%H%M%S",
        "use_microseconds": False,
        "default_extension": "md",
    }


def main():
    print("Installing AutoSaveNewFiles Sublime Text Plugin...")

    # Get the Packages directory
    packages_dir = get_sublime_packages_dir()
    if not os.path.exists(packages_dir):
        print(f"Error: Sublime Text Packages directory not found at {packages_dir}")
        print("Please make sure Sublime Text is installed correctly.")
        sys.exit(1)

    # Create User directory if it doesn't exist
    user_dir = os.path.join(packages_dir, "User")
    os.makedirs(user_dir, exist_ok=True)

    # Get the current directory (where the install script is)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Copy plugin file
    plugin_src = os.path.join(current_dir, "auto_save_new_files.py")
    plugin_dst = os.path.join(user_dir, "auto_save_new_files.py")

    try:
        shutil.copy2(plugin_src, plugin_dst)
        print(f"✓ Copied plugin file to {plugin_dst}")
    except Exception as e:
        print(f"Error copying plugin file: {e}")
        sys.exit(1)

    # Create settings file if it doesn't exist
    settings_file = os.path.join(user_dir, "AutoSaveNewFiles.sublime-settings")
    if not os.path.exists(settings_file):
        try:
            with open(settings_file, "w") as f:
                json.dump(create_default_config(), f, indent=2)
            print(f"✓ Created settings file at {settings_file}")
        except Exception as e:
            print(f"Error creating settings file: {e}")
            sys.exit(1)
    else:
        print(f"! Settings file already exists at {settings_file}")

    # Create default scratch directory
    scratch_dir = os.path.expanduser("~/scratch")
    os.makedirs(scratch_dir, exist_ok=True)
    print(f"✓ Created scratch directory at {scratch_dir}")

    print("\nInstallation complete! 🎉")
    print("\nNext steps:")
    print("1. Restart Sublime Text if it's running")
    print("2. Open the settings file to customize:")
    print(f"   {settings_file}")
    print("3. Start using the plugin by creating new files in Sublime Text")
    print("\nFor more information, see the README.md file.")


if __name__ == "__main__":
    main()
