# Colorful Nmap Scanner

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python script that enhances nmap's version scanning (`-sV`) by highlighting deprecated or outdated software versions in red. This tool helps security professionals and system administrators quickly identify potentially vulnerable services during network scans.

![Screenshot](screenshot.png)

## Features

- Runs nmap with version detection (`-sV`)
- Colorizes the output for better readability
- Highlights deprecated/old software versions in red
- Supports all standard nmap arguments
- Checks if nmap is installed and provides installation instructions if needed
- Includes a comprehensive database of deprecated software versions

## Requirements

- Python 3.6+
- nmap
- packaging library (`pip install packaging`)

## Installation

1. Make sure you have nmap installed:
   - macOS: `brew install nmap`
   - Ubuntu/Debian: `sudo apt-get install nmap`
   - CentOS/RHEL: `sudo yum install nmap`
   - Windows: Download from [nmap.org](https://nmap.org/download.html)

2. Install the required Python package:
   ```
   pip install packaging
   ```

3. Make the script executable:
   ```
   chmod +x colorful_nmap.py
   ```

## Usage

Basic usage:
```
python colorful_nmap.py [target]
```

Examples:
```
# Scan a single host
python colorful_nmap.py 192.168.1.1

# Scan specific ports
python colorful_nmap.py -p 22,80,443 example.com

# Scan top 100 ports
python colorful_nmap.py --top-ports 100 192.168.1.0/24

# Aggressive scan
python colorful_nmap.py -A example.com
```

## How It Works

The script:
1. Runs nmap with version detection
2. Parses the output to identify software and version information
3. Compares detected versions against a database of known deprecated versions
4. Highlights outdated versions in red
5. Applies additional color formatting to improve readability

## Color Legend

- **Red**: Deprecated/outdated software versions
- **Cyan**: Port numbers
- **Green**: Port states
- **Blue**: Headers and scan information
- **Purple**: Host status information
- **Yellow**: MAC addresses
- **Bold**: Important headers and information

## Customization

You can modify the `DEPRECATED_VERSIONS` dictionary in the script to update the list of deprecated software versions according to your security requirements.

## Contributing

Contributions are welcome! Here are some ways you can contribute:

- Report bugs and issues
- Add new features or enhancements
- Update the deprecated versions database
- Improve documentation

## Security Considerations

Please note that the deprecated versions database included in this tool is not an official security database and may not be complete or up-to-date. It should be used as a helpful indicator, not as a definitive security assessment tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
