# Contributing to AutoSaveNewFiles

First off, thank you for considering contributing to AutoSaveNewFiles!

## Development Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Setting Up Development Environment

1. Install `just` command runner:

   ```bash
   # macOS
   brew install just

   # Linux
   curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash
   ```

2. Clone your fork:

   ```bash
   git clone https://github.com/YOUR_USERNAME/AutoSaveScratch.git
   cd AutoSaveScratch
   ```

3. Set up the development environment:
   ```bash
   just setup
   ```

## Development Commands

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
```

## Code Style

- Use Black for formatting (line length: 100)
- Follow PEP 8 guidelines
- Add type hints to all functions
- Write descriptive docstrings
- Keep functions focused and small

## Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the version numbers following [Semantic Versioning](http://semver.org/)
3. Ensure all checks pass (`just check`)
4. The PR will be merged once you have the sign-off

## Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters
- Reference issues and pull requests after the first line

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
