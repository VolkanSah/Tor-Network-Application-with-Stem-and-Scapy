# Tor Network Application with Stem and Scapy

This project demonstrates how to use the Stem library to interact with the Tor network and the Scapy library for network packet manipulation. The goal is to create an application that can leverage Tor for anonymized network analysis.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Connecting to a Running Tor Process](#connecting-to-a-running-tor-process)
  - [Starting a New Tor Process](#starting-a-new-tor-process)
  - [Sending Packets through Tor with Scapy](#sending-packets-through-tor-with-scapy)
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

## Credits
- [VolkanSah on Github](https://github.com/volkansah)
- [Developer Site](https://volkansah.github.io)
- [Become a 'Sponsor'](https://github.com/sponsors/volkansah)
- [Source of this resposerity](https://github.com/VolkanSah/Tor-Network-Application-with-Stem-and-Scapy)

### License

This project is licensed under the MIT License. 
