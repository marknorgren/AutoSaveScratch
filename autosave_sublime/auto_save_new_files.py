"""
AutoSaveNewFiles - Sublime Text Plugin

This plugin automatically saves new empty files with timestamp-based names
in a designated directory. It provides configurable options for file naming,
timestamp formats, and automatic file management.

Classes:
    AutoSaveNewFilesCommand: Main plugin class that handles file operations

Author: Mark
License: MIT
"""

import datetime
import os
from typing import Dict, Set

import sublime
import sublime_plugin

# Define a global debug flag
DEBUG = False  # Set to True to enable debug logging


def debug_log(message: str) -> None:
    """
    Log debug messages if DEBUG is enabled.

    Args:
        message: The message to log
    """
    if DEBUG:
        print("[AutoSaveNewFiles] " + message)


class AutoSaveNewFilesCommand(sublime_plugin.EventListener):
    """
    Main plugin class that handles automatic file saving and management.

    This class listens for various Sublime Text events to automatically save new
    empty files with timestamp-based names and manage their lifecycle.

    Attributes:
        saved_files: Set of files managed by this plugin
        file_timestamps: Dictionary mapping file paths to their timestamps
    """

    def __init__(self):
        """Initialize the plugin with empty tracking collections."""
        self.saved_files: Set[str] = set()
        self.file_timestamps: Dict[str, str] = {}

    def on_new_async(self, view: sublime.View) -> None:
        """Handle new file creation events."""
        self.save_new_file_with_timestamp(view)

    def on_activated_async(self, view: sublime.View) -> None:
        """Handle file activation events."""
        self.save_new_file_with_timestamp(view)

    def on_load_async(self, view: sublime.View) -> None:
        """Handle file load events."""
        self.save_new_file_with_timestamp(view)

    def on_pre_close(self, view: sublime.View) -> None:
        """Handle file closing events."""
        self.check_and_delete_empty_file(view)

    def save_new_file_with_timestamp(self, view: sublime.View) -> None:
        """
        Save a new empty file with a timestamp-based name.

        Args:
            view: The Sublime Text view to save

        This method handles the main logic for saving new files:
        - Checks if the file should be saved
        - Loads plugin settings
        - Generates timestamp and filename
        - Creates the save directory if needed
        - Saves the file and optionally inserts a timestamp
        """
        if view.file_name() in self.saved_files or view.file_name() is not None:
            return

        if (
            not view.is_scratch()
            and view.file_name() is None
            and len(view.substr(sublime.Region(0, view.size()))) == 0
        ):
            # Load settings with defaults
            settings = sublime.load_settings("AutoSaveNewFiles.sublime-settings")
            save_directory = os.path.expanduser(settings.get("save_directory", "~/scratch"))
            filename_format = settings.get("filename_format", "{timestamp}.{extension}")
            insert_timestamp = settings.get("insert_timestamp", True)
            timestamp_format = settings.get("timestamp_format", "%Y_%m_%d_%H%M%S")
            use_microseconds = settings.get("use_microseconds", False)
            default_extension = settings.get("default_extension", "md")

            debug_log(f"Save directory: {save_directory}")

            # Ensure we have proper permissions for the save directory
            try:
                # Create the directory if it doesn't exist
                if not os.path.exists(save_directory):
                    os.makedirs(save_directory)
                    debug_log("Directory created.")

                # Test write permissions
                test_file = os.path.join(save_directory, ".test_permissions")
                with open(test_file, "w") as f:
                    f.write("")
                os.remove(test_file)
            except PermissionError:
                error_msg = f"Permission denied: Cannot access directory {save_directory}"
                debug_log(error_msg)
                sublime.error_message(f"AutoSaveNewFiles: {error_msg}")
                return
            except OSError as e:
                error_msg = f"Failed to access directory {save_directory}: {str(e)}"
                debug_log(error_msg)
                sublime.error_message(f"AutoSaveNewFiles: {error_msg}")
                return

            # Generate timestamp
            now = datetime.datetime.now()
            if use_microseconds:
                timestamp = now.strftime(f"{timestamp_format}_%f")[:-3]
            else:
                timestamp = now.strftime(timestamp_format)

            # Generate filename
            filename = filename_format.format(timestamp=timestamp, extension=default_extension)
            debug_log(f"Generated filename: {filename}")

            # Construct the full file path
            file_path = os.path.join(save_directory, filename)
            debug_log(f"Full file path: {file_path}")

            # Handle filename conflicts
            counter = 1
            while os.path.exists(file_path):
                base, ext = os.path.splitext(filename)
                new_filename = f"{base}_{counter}{ext}"
                file_path = os.path.join(save_directory, new_filename)
                counter += 1

            # Save the new file
            try:
                view.retarget(file_path)
                view.run_command("save")
                debug_log(f"File saved: {file_path}")

                # Insert the timestamp as the first line if enabled
                if insert_timestamp:
                    view.run_command("insert", {"characters": timestamp + "\n"})
                    debug_log(f"Timestamp added to file: {file_path}")
                    view.run_command("save")

                self.saved_files.add(file_path)
                self.file_timestamps[file_path] = timestamp
            except Exception as e:
                debug_log(f"Failed to save file: {e}")
                sublime.error_message(
                    f"AutoSaveNewFiles: Failed to save file {file_path}\nError: {str(e)}"
                )

    def check_and_delete_empty_file(self, view: sublime.View) -> None:
        """
        Check if a file is empty and delete it if necessary.

        Args:
            view: The Sublime Text view to check

        This method is called when a file is being closed. It checks if:
        - The file was created by this plugin
        - The file is empty or contains only a timestamp
        If both conditions are met, the file is deleted.
        """
        file_path = view.file_name()
        if file_path in self.saved_files:
            content = view.substr(sublime.Region(0, view.size())).strip()
            timestamp = self.file_timestamps.get(file_path, "")

            if content == timestamp or not content:
                try:
                    os.remove(file_path)
                    debug_log(f"Deleted empty file: {file_path}")
                    self.saved_files.remove(file_path)
                    del self.file_timestamps[file_path]
                except PermissionError:
                    error_msg = f"Permission denied: Cannot delete file {file_path}"
                    debug_log(error_msg)
                    sublime.error_message(f"AutoSaveNewFiles: {error_msg}")
                except OSError as e:
                    error_msg = f"Failed to delete file {file_path}: {str(e)}"
                    debug_log(error_msg)
                    sublime.error_message(f"AutoSaveNewFiles: {error_msg}")
            else:
                debug_log(f"File not empty, keeping: {file_path}")


# Save this file as auto_save_new_files.py in the Packages/User directory.
