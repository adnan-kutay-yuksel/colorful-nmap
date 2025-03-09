# Contributing to Colorful Nmap Scanner

Thank you for considering contributing to the Colorful Nmap Scanner! This document provides guidelines and instructions for contributing to this project.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with the following information:
- A clear, descriptive title
- Steps to reproduce the bug
- Expected behavior
- Actual behavior
- Any relevant logs or screenshots

### Suggesting Enhancements

For feature requests, please create an issue with:
- A clear, descriptive title
- Detailed description of the proposed feature
- Any relevant examples or mockups

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Run tests if applicable
5. Commit your changes (`git commit -m 'Add new feature'`)
6. Push to the branch (`git push origin feature-branch`)
7. Open a Pull Request

## Development Setup

1. Clone the repository
2. Install dependencies: `pip install packaging`
3. Make sure nmap is installed on your system

## Updating the Deprecated Versions Database

The `DEPRECATED_VERSIONS` dictionary in `colorful_nmap.py` contains the database of software versions considered deprecated. When updating this database:

1. Use reliable sources for EOL (End of Life) information
2. Include a comment with the source of the information
3. Consider adding the date when the information was last updated

## Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Write docstrings for functions and classes

## License

By contributing to this project, you agree that your contributions will be licensed under the project's MIT License.
