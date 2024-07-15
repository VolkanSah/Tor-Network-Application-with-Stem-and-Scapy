# Tor Network Application with Stem and Scapy (TNASS)
###### update 07/2024
![TNA-SS](tnass.jpg)
Security comes at a high price in life. Freedom, security, and democracy are not guaranteed. Small tools always bring advantages to the user that can be used to automate processes. These creative scripts aim to show you how simple functions can save a lot of time and money, eliminating the need to purchase expensive security packages for basic scanning tasks.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Connecting to a Running Tor Process](#connecting-to-a-running-tor-process)
  - [Starting a New Tor Process](#starting-a-new-tor-process)
  - [Sending Packets through Tor with Scapy](#sending-packets-through-tor-with-scapy)
  - [Single Domain Security Check](#single-domain-security-check)
  - [Multiple Domains Security Check from File](#multiple-domains-security-check-from-file)
- [Credits](#credits)
- [License](#license)

## Introduction

This project provides an example of how to use Python libraries Stem and Scapy to work with the Tor network. Stem is a library for interacting with Tor, while Scapy is used for creating and manipulating network packets. Together, they allow for anonymized network operations.

## Requirements

- Python 3.x
- Stem
- Scapy
- Tor

## Installation

1. Install Python 3.x from [Python's official website](https://www.python.org/).
2. Install Stem using pip:
    ```bash
    pip install stem
    ```
3. Install Scapy using pip:
    ```bash
    pip install scapy
    ```
4. Ensure Tor is installed and running. You can download and install Tor from [Tor Project's official website](https://www.torproject.org/).

## Usage

### Connecting to a Running Tor Process

To connect to an existing Tor process and retrieve basic information:

```python
from stem import Signal
from stem.control import Controller

with Controller.from_port(port = 9051) as controller:
    controller.authenticate()  # Authenticate if necessary
    
    print("Tor Version:", controller.get_version())
    print("Allowed SocksPort:", controller.get_conf("SocksPort"))
    
    # Request a new identity
    controller.signal(Signal.NEWNYM)
    print("New identity requested")
```

### Starting a New Tor Process

To start a new Tor process directly from your Python script:

```python
from stem.process import launch_tor_with_config

tor_process = launch_tor_with_config(
    config = {
        'SocksPort': '9050',
        'ControlPort': '9051',
    },
    init_msg_handler = lambda line: print(line),
)

print("Tor process started")

# Terminate the Tor process
tor_process.terminate()
``` 

### Sending Packets through Tor with Scapy

To send network packets through the Tor network using Scapy:

```python
from scapy.all import *
import socks
import socket

# Set up Tor Socks proxy
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

# Create and send a simple ICMP packet
packet = IP(dst="8.8.8.8")/ICMP()
response = sr1(packet, timeout=10)

if response:
    response.show()
else:
    print("No response received")
```

### Single Domain Security Check

The `single.py` script starts a Tor process, requests a new Tor identity, and performs security checks on a specified domain (both Onion and regular websites) using various tools. The script runs the following steps:

1. **Start Tor Process:** Initializes a Tor process with a specified configuration for `SocksPort` and `ControlPort`.
2. **Authenticate with Tor Controller:** Connects to the Tor control port and authenticates.
3. **Request New Identity:** Requests a new Tor identity using the `NEWNYM` signal.
4. **Perform Security Checks:** Executes security tools (`nmap`, `nikto`, `socat`) on the specified domain and prints the results.
5. **Terminate Tor Process:** Ends the Tor process after completing the checks.

### Multiple Domains Security Check from File

The `from_file.py` script extends the functionality of `single.py` by reading multiple domains from a text or CSV file and performing security checks on each. The script follows these steps:

1. **Start Tor Process:** Initializes a Tor process with a specified configuration for `SocksPort` and `ControlPort`.
2. **Authenticate with Tor Controller:** Connects to the Tor control port and authenticates.
3. **Read Domains from File:** Reads a list of domains from a text or CSV file.
4. **Iterate Over Domains:**
   - Requests a new Tor identity for each domain.
   - Executes security tools (`nmap`, `nikto`, `socat`) on each domain and prints the results.
5. **Terminate Tor Process:** Ends the Tor process after processing all domains.

## Possible Automation with These Scripts

These scripts can be used to automate security testing of both Onion and regular domains. They demonstrate how to:
- Integrate Tor with security tools.
- Automate the process of changing Tor identities.
- Perform repeated security checks on multiple domains.

Additional tools and tasks that could be automated with similar scripts include:
- Vulnerability scanning with other tools like OpenVAS.
- Web application security testing with OWASP ZAP.
- Network traffic analysis with Wireshark.
- Automated penetration testing with Metasploit.

By leveraging these scripts, various security testing and network analysis tasks can be performed automatically within the Tor network.

## Your Support
If you find this project useful and want to support it, there are several ways to do so:

- If you find the white paper helpful, please ⭐ it on GitHub. This helps make the project more visible and reach more people.
- Become a Follower: If you're interested in updates and future improvements, please follow my GitHub account. This way you'll always stay up-to-date.
- Learn more about my work: I invite you to check out all of my work on GitHub and visit my developer site https://volkansah.github.io. Here you will find detailed information about me and my projects.
- Share the project: If you know someone who could benefit from this project, please share it. The more people who can use it, the better.
**If you appreciate my work and would like to support it, please visit my [GitHub Sponsor page](https://github.com/sponsors/volkansah). Any type of support is warmly welcomed and helps me to further improve and expand my work.**

Thank you for your support! ❤️

### Credits
S. Volkan Kücükbudak
- [Source of this repository](https://github.com/VolkanSah/Tor-Network-Application-with-Stem-and-Scapy)

### License

This project is licensed under the MIT License.

