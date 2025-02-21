#!/usr/bin/env python3
"""
Setup script for AutoSaveNewFiles Sublime Text Plugin.
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
from typing import List, Optional, Tuple


def get_sublime_packages_dirs() -> List[str]:
    """
    Get potential Sublime Text Packages directories based on the OS.
    Returns a list of possible paths, ordered by preference (newest version first).
    """
    home = str(Path.home())

    if sys.platform == "darwin":  # macOS
        return [
            os.path.join(home, "Library", "Application Support", "Sublime Text", "Packages"),
            os.path.join(home, "Library", "Application Support", "Sublime Text 3", "Packages"),
            os.path.join(home, "Library", "Application Support", "Sublime Text 2", "Packages"),
        ]
    elif sys.platform == "win32":  # Windows
        return [
            os.path.join(os.getenv("APPDATA", ""), "Sublime Text", "Packages"),
            os.path.join(os.getenv("APPDATA", ""), "Sublime Text 3", "Packages"),
            os.path.join(os.getenv("APPDATA", ""), "Sublime Text 2", "Packages"),
        ]
    else:  # Linux
        return [
            os.path.join(home, ".config", "sublime-text", "Packages"),
            os.path.join(home, ".config", "sublime-text-3", "Packages"),
            os.path.join(home, ".config", "sublime-text-2", "Packages"),
        ]


def get_first_valid_sublime_dir() -> Optional[str]:
    """Find the first valid Sublime Text Packages directory."""
    for dir_path in get_sublime_packages_dirs():
        if os.path.exists(dir_path):
            return dir_path
    return None


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


def validate_directory(path: str) -> bool:
    """
    Validate if a directory is writable.

    Args:
        path: Directory path to validate

    Returns:
        bool: True if directory is writable, False otherwise
    """
    try:
        test_file = os.path.join(path, ".test_permissions")
        with open(test_file, "w") as f:
            f.write("")
        os.remove(test_file)
        return True
    except (PermissionError, OSError):
        return False


def setup_user_directory(packages_dir: str) -> Tuple[bool, str]:
    """
    Set up the User directory in Sublime Text Packages.

    Args:
        packages_dir: Path to Sublime Text Packages directory

    Returns:
        Tuple[bool, str]: Success status and user directory path
    """
    user_dir = os.path.join(packages_dir, "User")
    try:
        os.makedirs(user_dir, exist_ok=True)
        if not validate_directory(user_dir):
            return False, f"Cannot write to {user_dir}"
        return True, user_dir
    except Exception as e:
        return False, f"Error creating User directory: {e}"


def copy_plugin_file(package_dir: str, user_dir: str) -> Tuple[bool, str]:
    """
    Copy the plugin file to Sublime Text User directory.

    Args:
        package_dir: Source package directory
        user_dir: Destination user directory

    Returns:
        Tuple[bool, str]: Success status and message
    """
    plugin_src = os.path.join(package_dir, "auto_save_new_files.py")
    plugin_dst = os.path.join(user_dir, "auto_save_new_files.py")
    try:
        shutil.copy2(plugin_src, plugin_dst)
        return True, f"✓ Copied plugin file to {plugin_dst}"
    except Exception as e:
        return False, f"Error copying plugin file: {e}"


def create_settings(user_dir: str) -> Tuple[bool, str]:
    """
    Create the settings file if it doesn't exist.

    Args:
        user_dir: Sublime Text User directory

    Returns:
        Tuple[bool, str]: Success status and message
    """
    settings_file = os.path.join(user_dir, "AutoSaveNewFiles.sublime-settings")
    if not os.path.exists(settings_file):
        try:
            with open(settings_file, "w") as f:
                json.dump(create_default_config(), f, indent=2)
            return True, f"✓ Created settings file at {settings_file}"
        except Exception as e:
            return False, f"Error creating settings file: {e}"
    return True, f"! Settings file already exists at {settings_file}"


def setup_scratch_directory() -> str:
    """Set up the scratch directory and return status message."""
    scratch_dir = os.path.expanduser("~/scratch")
    try:
        os.makedirs(scratch_dir, exist_ok=True)
        if validate_directory(scratch_dir):
            return f"✓ Created scratch directory at {scratch_dir}"
        return f"! Warning: Cannot write to scratch directory at {scratch_dir}"
    except Exception as e:
        return f"! Warning: Failed to create scratch directory: {e}"


def main():
    """Main setup function."""
    print("Setting up AutoSaveNewFiles Sublime Text Plugin...")

    try:
        # Get package installation directory
        import autosave_sublime

        package_dir = os.path.dirname(autosave_sublime.__file__)
    except ImportError:
        print("Error: Package not found. Please install with:")
        print("pip install git+https://github.com/marknorgren/AutoSaveScratch.git")
        sys.exit(1)

    # Get the Packages directory
    packages_dir = get_first_valid_sublime_dir()
    if not packages_dir:
        print("Error: No valid Sublime Text installation found.")
        print("Looked in the following locations:")
        for dir_path in get_sublime_packages_dirs():
            print(f"  - {dir_path}")
        print("\nPlease make sure Sublime Text is installed correctly.")
        sys.exit(1)

    # Set up User directory
    success, user_dir = setup_user_directory(packages_dir)
    if not success:
        print(user_dir)  # Error message
        sys.exit(1)

    # Copy plugin file
    success, message = copy_plugin_file(package_dir, user_dir)
    print(message)
    if not success:
        sys.exit(1)

    # Create settings file
    success, message = create_settings(user_dir)
    print(message)
    if not success:
        sys.exit(1)

    # Set up scratch directory
    print(setup_scratch_directory())

    print("\nSetup complete! 🎉")
    print("\nNext steps:")
    print("1. Restart Sublime Text if it's running")
    print("2. Open the settings file to customize:")
    print(f"   {os.path.join(user_dir, 'AutoSaveNewFiles.sublime-settings')}")
    print("3. Start using the plugin by creating new files in Sublime Text")
    print("\nFor more information, see the README.md file.")


if __name__ == "__main__":
    main()
