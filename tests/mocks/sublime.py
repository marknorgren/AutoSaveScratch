"""Mock sublime module for testing."""


class Region:
    """Mock Region class."""

    def __init__(self, a, b=None):
        self.a = a
        self.b = b if b is not None else a


class View:
    """Mock View class."""

    def __init__(self):
        self._file_name = None
        self._is_scratch = False
        self._content = ""
        self._size = 0

    def file_name(self):
        return self._file_name

    def is_scratch(self):
        return self._is_scratch

    def size(self):
        return self._size

    def substr(self, region):
        return self._content

    def retarget(self, new_path):
        self._file_name = new_path

    def run_command(self, cmd, args=None):
        if cmd == "save":
            pass  # Mock save operation
        elif cmd == "insert" and args and "characters" in args:
            self._content += args["characters"]
            self._size = len(self._content)


def load_settings(settings_file):
    """Mock settings loader."""
    return Settings()


def error_message(message):
    """Mock error message display."""
    pass


class Settings:
    """Mock Settings class."""

    def __init__(self):
        self._settings = {
            "save_directory": "~/scratch",
            "filename_format": "{timestamp}.{extension}",
            "insert_timestamp": True,
            "timestamp_format": "%Y_%m_%d_%H%M%S",
            "use_microseconds": False,
            "default_extension": "md",
        }

    def get(self, key, default=None):
        return self._settings.get(key, default)
