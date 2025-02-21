#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

REPO="marknorgren/AutoSaveScratch"

echo -e "${BLUE}Installing AutoSaveNewFiles Sublime Text Plugin...${NC}"

# Detect OS and set paths
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    SUBLIME_PACKAGES="$HOME/Library/Application Support/Sublime Text/Packages"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    SUBLIME_PACKAGES="$HOME/.config/sublime-text/Packages"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows
    SUBLIME_PACKAGES="$APPDATA/Sublime Text/Packages"
else
    echo -e "${RED}Unsupported operating system${NC}"
    exit 1
fi

# Create plugin directory
PLUGIN_DIR="$SUBLIME_PACKAGES/AutoSaveNewFiles"
echo -e "${BLUE}Creating plugin directory: ${NC}$PLUGIN_DIR"
mkdir -p "$PLUGIN_DIR"

# Create scratch directory
SCRATCH_DIR="$HOME/scratch"
echo -e "${BLUE}Creating scratch directory: ${NC}$SCRATCH_DIR"
mkdir -p "$SCRATCH_DIR"

# Download plugin files
echo -e "${BLUE}Downloading plugin files...${NC}"

# Function to download a file
download_file() {
    local file=$1
    local output=$2
    local url="https://raw.githubusercontent.com/${REPO}/main/${file}"
    echo -e "${BLUE}Downloading: ${NC}${url}"
    echo -e "${BLUE}To: ${NC}${output}"
    curl -fsSL "$url" -o "$output"
    if [ $? -ne 0 ]; then
        echo -e "${RED}Failed to download: ${NC}${url}"
        return 1
    fi
    echo -e "${GREEN}Successfully downloaded: ${NC}${file}"
    return 0
}

# Download each file
download_file "autosave_sublime/auto_save_new_files.py" "$PLUGIN_DIR/auto_save_new_files.py" || exit 1
download_file "autosave_sublime/__init__.py" "$PLUGIN_DIR/__init__.py" || exit 1
download_file "AutoSaveNewFiles.sublime-settings" "$PLUGIN_DIR/AutoSaveNewFiles.sublime-settings" || exit 1

# Check if files were downloaded successfully
if [ ! -f "$PLUGIN_DIR/auto_save_new_files.py" ] || [ ! -f "$PLUGIN_DIR/__init__.py" ] || [ ! -f "$PLUGIN_DIR/AutoSaveNewFiles.sublime-settings" ]; then
    echo -e "${RED}Failed to download plugin files${NC}"
    exit 1
fi

echo -e "${GREEN}Installation complete!${NC}"
echo -e "${BLUE}Plugin installed to: ${NC}$PLUGIN_DIR"
echo -e "${BLUE}Scratch directory created at: ${NC}$SCRATCH_DIR"
echo -e "${GREEN}Please restart Sublime Text to activate the plugin.${NC}" 