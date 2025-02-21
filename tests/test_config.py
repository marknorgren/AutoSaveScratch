"""Tests for configuration handling."""

import datetime
import json
import os
import shutil
import sys
from pathlib import Path

# Add mocks directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "mocks"))

import sublime


def test_default_config():
    """Test that default configuration is valid."""
    settings = {
        "save_directory": "~/scratch",
        "filename_format": "{timestamp}.{extension}",
        "insert_timestamp": True,
        "timestamp_format": "%Y_%m_%d_%H%M%S",
        "use_microseconds": False,
        "default_extension": "md",
    }

    # Write test settings
    settings_dir = Path(__file__).parent / "test_data"
    settings_dir.mkdir(exist_ok=True)
    settings_file = settings_dir / "AutoSaveNewFiles.sublime-settings"
    with open(settings_file, "w") as f:
        json.dump(settings, f)

    assert os.path.exists(settings_file)

    # Test loading settings
    test_settings = sublime.load_settings("AutoSaveNewFiles.sublime-settings")
    assert test_settings.get("save_directory") == settings["save_directory"]
    assert test_settings.get("filename_format") == settings["filename_format"]
    assert test_settings.get("insert_timestamp") == settings["insert_timestamp"]

    # Clean up
    if settings_dir.exists():
        shutil.rmtree(settings_dir)


def test_timestamp_format():
    """Test that timestamp formatting works correctly."""
    # Test without microseconds
    now = datetime.datetime(2024, 3, 19, 12, 34, 56)
    settings = {"timestamp_format": "%Y_%m_%d_%H%M%S", "use_microseconds": False}
    expected = "2024_03_19_123456"
    result = now.strftime(settings["timestamp_format"])
    assert result == expected

    # Test with microseconds
    settings["use_microseconds"] = True
    now = datetime.datetime(2024, 3, 19, 12, 34, 56, 123000)  # Set microseconds to 123000
    expected = "2024_03_19_123456_123"
    result = now.strftime(f"{settings['timestamp_format']}_%f")[:-3]
    assert result == expected


def test_view_operations():
    """Test view operations with mock sublime.View."""
    view = sublime.View()

    # Test initial state
    assert view.file_name() is None
    assert not view.is_scratch()
    assert view.size() == 0

    # Test content operations
    view.run_command("insert", {"characters": "test content"})
    assert view.size() == len("test content")
    assert view.substr(sublime.Region(0, view.size())) == "test content"

    # Test file operations
    view.retarget("/test/path.md")
    assert view.file_name() == "/test/path.md"
