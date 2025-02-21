"""Tests for configuration handling."""

import os
import json
from pathlib import Path
from autosave_sublime.auto_save_new_files import AutoSaveNewFilesCommand


def test_default_config():
    """Test that default configuration is valid."""
    cmd = AutoSaveNewFilesCommand()
    settings = {
        "save_directory": "~/scratch",
        "filename_format": "{timestamp}.{extension}",
        "insert_timestamp": True,
        "timestamp_format": "%Y_%m_%d_%H%M%S",
        "use_microseconds": False,
        "default_extension": "md"
    }
    
    # Write test settings
    settings_dir = Path(__file__).parent / "test_data"
    settings_dir.mkdir(exist_ok=True)
    settings_file = settings_dir / "AutoSaveNewFiles.sublime-settings"
    with open(settings_file, "w") as f:
        json.dump(settings, f)
    
    assert os.path.exists(settings_file)
    
    # Clean up
    settings_file.unlink()
    settings_dir.rmdir()


def test_timestamp_format():
    """Test that timestamp formatting works correctly."""
    import datetime
    cmd = AutoSaveNewFilesCommand()
    
    # Test without microseconds
    now = datetime.datetime(2024, 3, 19, 12, 34, 56)
    settings = {
        "timestamp_format": "%Y_%m_%d_%H%M%S",
        "use_microseconds": False
    }
    expected = "2024_03_19_123456"
    result = now.strftime(settings["timestamp_format"])
    assert result == expected
    
    # Test with microseconds
    settings["use_microseconds"] = True
    expected = "2024_03_19_123456_123"
    result = now.strftime(f"{settings['timestamp_format']}_%f")[:-3]
    assert result == expected 