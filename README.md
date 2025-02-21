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

## Installation

### Quick Install (Recommended)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/marknorgren/AutoSaveScratch/main/install.sh)"
```

This will:

- Install the plugin in your Sublime Text Packages directory
- Create the default scratch directory
- Set up default configuration

### Manual Installation

If you prefer to install manually, you can:

1. Locate your Sublime Text Packages directory:

   - macOS: `~/Library/Application Support/Sublime Text/Packages/`
   - Windows: `%APPDATA%\Sublime Text\Packages\`
   - Linux: `~/.config/sublime-text/Packages/`

2. Clone the repository:

   ```bash
   git clone https://github.com/marknorgren/AutoSaveScratch.git "AutoSaveNewFiles"
   ```

3. Create the scratch directory:

   ```bash
   mkdir ~/scratch
   ```

4. Restart Sublime Text

The installation will automatically:

- Set up the plugin in the correct location
- Create default configuration
- Set up the scratch directory

## Configuration

The plugin uses these default settings:

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

To customize, create `Packages/User/AutoSaveNewFiles.sublime-settings` with your preferred settings.

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

1. Clone the repository:

   ```bash
   git clone https://github.com/marknorgren/AutoSaveScratch.git
   cd AutoSaveScratch
   ```

2. Set up the development environment:

   ```bash
   # Create and activate virtual environment
   python3 -m venv .venv
   source .venv/bin/activate

   # Install development tools
   pip install black ruff
   ```

### Code Style

This project uses:

- Black for code formatting (line length: 100)
- Ruff for linting and import sorting
- Type hints for better code clarity

### Making Changes

1. Create a new branch for your changes
2. Make your changes and ensure they pass formatting and linting checks
3. Test the plugin in Sublime Text
4. Submit a pull request with your improvements

## License

MIT License - Feel free to modify and distribute as needed.
