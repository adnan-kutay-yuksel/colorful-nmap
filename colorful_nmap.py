#!/usr/bin/env python3
"""
Colorful Nmap Scanner - Highlights deprecated/old versions in red
"""

import subprocess
import re
import sys
import os
import platform
from datetime import datetime
import argparse
from packaging import version

# ANSI color codes
class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"

# Dictionary of known software with their deprecated versions
# Format: 'software_name': 'last_deprecated_version'
DEPRECATED_VERSIONS = {
    'OpenSSH': '7.9',
    'Apache': '2.4.38',
    'nginx': '1.16.0',
    'ProFTPD': '1.3.5',
    'vsftpd': '3.0.2',
    'MySQL': '5.7',
    'MariaDB': '10.3',
    'PostgreSQL': '10.0',
    'Microsoft-IIS': '8.5',
    'PHP': '7.3',
    'Postfix': '3.3',
    'Exim': '4.92',
    'Sendmail': '8.15',
    'Dovecot': '2.3.4',
    'Tomcat': '8.5',
    'Jenkins': '2.200',
    'MongoDB': '4.0',
    'Redis': '5.0',
    'Elasticsearch': '6.8',
    'Samba': '4.9',
    'OpenVPN': '2.4.7',
    'Drupal': '8.7',
    'WordPress': '5.2',
    'Joomla': '3.9',
    'Node.js': '12.0',
    'Python': '3.6',
    'Ruby': '2.5',
    'Perl': '5.26',
    'Java': '8',
    'OpenJDK': '8',
    'Lighttpd': '1.4.53',
    'Squid': '4.6',
    'Varnish': '6.1',
    'Memcached': '1.5',
    'RabbitMQ': '3.7',
    'Zookeeper': '3.4',
    'Kubernetes': '1.15',
    'Docker': '18.09',
    'Consul': '1.5',
    'Vault': '1.1',
    'Prometheus': '2.10',
    'Grafana': '6.2',
    'HAProxy': '1.9',
    'Traefik': '1.7',
    'Caddy': '1.0',
    'Bind': '9.11',
    'Unbound': '1.9',
    'PowerDNS': '4.1',
    'ISC DHCP': '4.4.1',
    'Puppet': '5.5',
    'Chef': '14.0',
    'Ansible': '2.8',
    'Salt': '2019.2',
    'GitLab': '11.11',
    'Subversion': '1.10',
    'Mercurial': '5.0',
    'OpenLDAP': '2.4.47',
    'FreeRADIUS': '3.0.17',
    'Asterisk': '16.3',
    'OpenSSL': '1.1.0',
    'LibreSSL': '2.8',
    'GnuTLS': '3.6.7',
    'Cyrus SASL': '2.1.26',
    'OpenSMTPD': '6.4',
    'Courier': '0.75',
    'Roundcube': '1.3',
    'Nextcloud': '15.0',
    'ownCloud': '10.1',
    'Magento': '2.3.1',
    'PrestaShop': '1.7.5',
    'WooCommerce': '3.6',
    'Shopify': '2.0',
    'Moodle': '3.6',
    'Canvas LMS': '1.0',
    'Blackboard': '9.1',
    'MediaWiki': '1.32',
    'DokuWiki': '2018-04-22',
    'Tiki Wiki': '19.0',
    'Confluence': '6.15',
    'JIRA': '8.1',
    'Redmine': '4.0',
    'Bugzilla': '5.0',
    'Trac': '1.2',
    'MantisBT': '2.21',
    'Splunk': '7.2',
    'Nagios': '4.4',
    'Zabbix': '4.2',
    'Icinga': '2.10',
    'Cacti': '1.2.0',
    'Munin': '2.0.47',
    'Kibana': '6.8',
    'Logstash': '6.8',
    'Graylog': '3.0',
    'Suricata': '4.1',
    'Snort': '2.9.12',
    'OSSEC': '3.1',
    'Fail2Ban': '0.10',
    'ModSecurity': '2.9',
    'Palo Alto': '8.1',
    'Cisco IOS': '15.6',
    'Juniper Junos': '18.4',
    'FortiOS': '6.0',
    'pfSense': '2.4.4',
    'OPNsense': '19.1',
    'VyOS': '1.2',
    'OpenWrt': '18.06',
    'DD-WRT': 'v3.0-r37305',
    'Tomato': '1.28',
    'OpenBSD': '6.4',
    'FreeBSD': '11.2',
    'NetBSD': '8.0',
    'Debian': '9.0',
    'Ubuntu': '18.04',
    'CentOS': '7.6',
    'RHEL': '7.6',
    'Fedora': '29',
    'SUSE': '15.0',
    'Windows Server': '2012 R2',
    'Windows': '8.1',
    'macOS': '10.14',
    'Android': '8.0',
    'iOS': '12.0'
}

def check_nmap_installed():
    """Check if nmap is installed on the system"""
    try:
        subprocess.run(["which", "nmap"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_nmap():
    """Provide instructions to install nmap based on the operating system"""
    system = platform.system()
    print(f"{Colors.YELLOW}Nmap is not installed on your system.{Colors.RESET}")
    
    if system == "Darwin":  # macOS
        print(f"{Colors.CYAN}To install nmap on macOS, you can use Homebrew:{Colors.RESET}")
        print("  brew install nmap")
    elif system == "Linux":
        print(f"{Colors.CYAN}To install nmap on Linux, use your package manager:{Colors.RESET}")
        print("  Ubuntu/Debian: sudo apt-get install nmap")
        print("  CentOS/RHEL: sudo yum install nmap")
        print("  Fedora: sudo dnf install nmap")
    elif system == "Windows":
        print(f"{Colors.CYAN}To install nmap on Windows:{Colors.RESET}")
        print("  1. Download the installer from https://nmap.org/download.html")
        print("  2. Run the installer and follow the instructions")
    
    print(f"\n{Colors.YELLOW}After installing nmap, run this script again.{Colors.RESET}")
    sys.exit(1)

def parse_version(version_str):
    """Parse version string to a comparable format"""
    # Extract the first version-like string from the input
    version_match = re.search(r'(\d+(\.\d+)*)', version_str)
    if version_match:
        try:
            return version.parse(version_match.group(1))
        except:
            return version.parse("0.0")
    return version.parse("0.0")

def is_deprecated(software, ver_str):
    """Check if the software version is deprecated"""
    # First, find the software in our deprecated versions dictionary
    for known_software, deprecated_ver in DEPRECATED_VERSIONS.items():
        if known_software.lower() in software.lower():
            try:
                # Parse the version strings
                current_version = parse_version(ver_str)
                deprecated_version = parse_version(deprecated_ver)
                
                # Compare versions
                return current_version <= deprecated_version
            except:
                # If we can't parse the version, assume it's not deprecated
                return False
    
    # If software not in our list, it's not considered deprecated
    return False

def colorize_nmap_output(line):
    """Colorize the nmap output line based on version information"""
    # Check if this is a service line with version info
    service_match = re.search(r'(\d+)\/(\w+)\s+(\w+)\s+(.+)', line)
    
    if service_match:
        port = service_match.group(1)
        protocol = service_match.group(2)
        state = service_match.group(3)
        service_info = service_match.group(4)
        
        # Extract service name and version
        service_parts = service_info.split()
        service_name = service_parts[0] if service_parts else ""
        
        # Check if there's version information
        version_match = re.search(r'([\w\.-]+)\s+(\d+(\.\d+)*)', service_info)
        if version_match:
            software_name = version_match.group(1)
            version_str = version_match.group(2)
            
            # Check if the version is deprecated
            if is_deprecated(software_name, version_str):
                # Highlight the entire service info in red
                service_info = f"{Colors.RED}{service_info}{Colors.RESET}"
        
        # Reconstruct the line with colors
        colored_line = f"{Colors.CYAN}{port}/{protocol}{Colors.RESET} {Colors.GREEN}{state}{Colors.RESET} {service_info}"
        return colored_line
    
    # If it's a header or other line, add some basic coloring
    if "Starting Nmap" in line or "Nmap scan report" in line:
        return f"{Colors.BOLD}{Colors.BLUE}{line}{Colors.RESET}"
    elif "Host is" in line:
        return f"{Colors.PURPLE}{line}{Colors.RESET}"
    elif "MAC Address" in line:
        return f"{Colors.YELLOW}{line}{Colors.RESET}"
    elif "PORT" in line and "STATE" in line and "SERVICE" in line:
        return f"{Colors.BOLD}{line}{Colors.RESET}"
    
    # Return the line unchanged if no specific coloring rules apply
    return line

def run_nmap_scan(target, additional_args=None):
    """Run nmap scan with version detection"""
    print(f"{Colors.BOLD}{Colors.BLUE}Starting Colorful Nmap Version Scanner{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}Target: {target}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'=' * 60}{Colors.RESET}\n")
    
    # Prepare the nmap command with version detection
    cmd = ["nmap", "-sV"]
    
    # Add any additional arguments
    if additional_args:
        cmd.extend(additional_args)
    
    # Add the target
    cmd.append(target)
    
    try:
        # Run the nmap command
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Process output line by line
        for line in process.stdout:
            line = line.strip()
            colored_line = colorize_nmap_output(line)
            print(colored_line)
        
        # Wait for the process to complete
        process.wait()
        
        # Check for errors
        if process.returncode != 0:
            stderr = process.stderr.read()
            print(f"{Colors.RED}Error running nmap: {stderr}{Colors.RESET}")
            return False
        
        return True
    
    except Exception as e:
        print(f"{Colors.RED}Error: {str(e)}{Colors.RESET}")
        return False

def main():
    """Main function"""
    # Check if nmap is installed
    if not check_nmap_installed():
        install_nmap()
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Colorful Nmap Scanner - Highlights deprecated/old versions in red")
    parser.add_argument("target", help="Target to scan (IP address, hostname, or network range)")
    parser.add_argument("-p", "--ports", help="Port specification (e.g., '80,443' or '1-1000')")
    parser.add_argument("-T", "--timing", choices=["0", "1", "2", "3", "4", "5"], 
                        help="Timing template (0=paranoid, 5=insane)")
    parser.add_argument("--top-ports", help="Scan only the N most common ports")
    parser.add_argument("-A", "--aggressive", action="store_true", 
                        help="Enable OS detection, version detection, script scanning, and traceroute")
    
    args = parser.parse_args()
    
    # Prepare additional arguments for nmap
    additional_args = []
    
    if args.ports:
        additional_args.extend(["-p", args.ports])
    
    if args.timing:
        additional_args.append(f"-T{args.timing}")
    
    if args.top_ports:
        additional_args.extend(["--top-ports", args.top_ports])
    
    if args.aggressive:
        additional_args.append("-A")
    
    # Run the scan
    run_nmap_scan(args.target, additional_args)

if __name__ == "__main__":
    main()
