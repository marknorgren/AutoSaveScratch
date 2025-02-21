# AutoSaveNewFiles - Sublime Text Plugin

A Sublime Text plugin that automatically saves new empty files with timestamp-based names in a designated directory. Perfect for quick notes and scratch files that you want to keep organized.

## Requirements

- Sublime Text 2, 3, or 4
- Python 3.8 or higher
- Write permissions for the Sublime Text Packages directory
- Write permissions for the configured save directory

## Features

- Automatically saves new empty files with timestamp-based names
- Configurable save directory and filename formats
- Option to insert timestamps at the beginning of files
- Automatically deletes empty files when closed
- Customizable timestamp formats
- Handles file naming conflicts

## Quick Install

### Using pip (Recommended)

```bash
pip install git+https://github.com/marknorgren/AutoSaveScratch.git
python -m autosave_sublime.setup
```

### Manual Installation

1. Download or clone this repository
2. Run the installation script:
   ```bash
   python install.py
   ```
3. Restart Sublime Text

The installation will automatically:

- Detect your Sublime Text Packages directory
- Copy the plugin file to the correct location
- Create default configuration
- Set up the scratch directory

## Configuration

Create `AutoSaveNewFiles.sublime-settings` with the following settings:

```json
{
  "save_directory": "~/scratch",
  "filename_format": "{timestamp}.{extension}",
  "insert_timestamp": true,
  "timestamp_format": "%Y_%m_%d_%H%M%S",
  "use_microseconds": false,
  "default_extension": "md"
}
```

### Settings Explained

- `save_directory`: Path where new files will be saved (defaults to ~/scratch)
- `filename_format`: Format for new filenames (uses {timestamp} and {extension} placeholders)
- `insert_timestamp`: Whether to insert timestamp at the start of new files (true/false)
- `timestamp_format`: Python datetime format for timestamps
- `use_microseconds`: Whether to include microseconds in timestamps (true/false)
- `default_extension`: Default file extension for new files (without the dot)

## Usage

1. Open a new file in Sublime Text
2. The plugin will automatically:
   - Save empty files to your configured directory
   - Name files using your configured format
   - Insert a timestamp if enabled
   - Delete empty files when closed
   - Preserve files with content

## Troubleshooting

### Installation Issues

1. **Plugin Not Found**

   - Verify Sublime Text's Packages directory exists
   - Check file permissions in the Packages directory
   - Try manual installation if automatic fails

2. **Settings Not Applied**

   - Check if settings file exists in the correct location
   - Verify JSON syntax in settings file
   - Restart Sublime Text after changes

3. **Files Not Saving**
   - Verify save directory exists and is writable
   - Check console for error messages
   - Ensure file is empty when created

### Common Error Messages

1. "Cannot access directory"

   - Check directory permissions
   - Verify the path exists
   - Try creating directory manually

2. "Failed to save file"

   - Check disk space
   - Verify write permissions
   - Check file path length

3. "Settings file not found"
   - Reinstall plugin
   - Create settings file manually
   - Check file location

## Debugging

To enable debug logging:

1. Open the plugin file (`auto_save_new_files.py`)
2. Set `DEBUG = True` at the top of the file
3. View logs in Sublime Text's console (View > Show Console)
4. Look for messages prefixed with `[AutoSaveNewFiles]`

## Development

To set up a development environment:

1. Install `just` command runner:

   ```bash
   # macOS
   brew install just

   # Linux
   curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash
   ```

2. Clone the repository:

   ```bash
   git clone https://github.com/marknorgren/AutoSaveScratch.git
   cd AutoSaveScratch
   ```

3. Set up the development environment:
   ```bash
   just setup
   ```

### Common Development Tasks

Use `just` commands to manage development tasks:

```bash
just                 # List all available commands
just setup          # Install development dependencies
just format         # Format code with black
just lint           # Run ruff linter
just check          # Run all checks (format and lint)
just fix            # Fix formatting and linting issues
just clean          # Clean up cache files
just install        # Install plugin in Sublime Text
just uninstall      # Remove plugin from Sublime Text
just test           # Run complete test cycle
just branch name    # Create a new feature branch
```

### Code Style

This project uses:

- Black for code formatting (line length: 100)
- Ruff for linting and import sorting
- Type hints for better code clarity

### Making Changes

1. Create a new branch:

   ```bash
   just branch feature-name
   ```

2. Make your changes and ensure they pass all checks:

   ```bash
   just check
   ```

3. Test the plugin:

   ```bash
   just test
   ```

4. Submit a pull request with your improvements

## License

MIT License - Feel free to modify and distribute as needed.
