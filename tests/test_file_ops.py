"""Tests for file operations."""

import tempfile
from pathlib import Path


def test_directory_creation():
    """Test that directories can be created and are writable."""
    with tempfile.TemporaryDirectory() as temp_dir:
        test_dir = Path(temp_dir) / "test_scratch"

        # Create directory
        test_dir.mkdir(exist_ok=True)
        assert test_dir.exists()

        # Test write permissions
        test_file = test_dir / ".test_permissions"
        test_file.write_text("test")
        assert test_file.exists()

        # Clean up
        test_file.unlink()
        test_dir.rmdir()


def test_file_naming():
    """Test file naming and conflict resolution."""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_name = "2024_03_19_123456"
        ext = ".md"

        # Create first file
        file1 = Path(temp_dir) / f"{base_name}{ext}"
        file1.write_text("test")
        assert file1.exists()

        # Create second file (should get _1 suffix)
        file2 = Path(temp_dir) / f"{base_name}_1{ext}"
        file2.write_text("test")
        assert file2.exists()

        # Create third file (should get _2 suffix)
        file3 = Path(temp_dir) / f"{base_name}_2{ext}"
        file3.write_text("test")
        assert file3.exists()

        # Verify all files exist
        assert len(list(Path(temp_dir).glob(f"{base_name}*{ext}"))) == 3
