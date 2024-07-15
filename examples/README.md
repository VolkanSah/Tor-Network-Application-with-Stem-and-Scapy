# Script Descriptions

## single.py

The `single.py` script starts a Tor process, requests a new Tor identity, and performs security checks on a specified Onion domain using various tools. The script runs the following steps:

1. **Start Tor Process:** Initializes a Tor process with a specified configuration for `SocksPort` and `ControlPort`.
2. **Authenticate with Tor Controller:** Connects to the Tor control port and authenticates.
3. **Request New Identity:** Requests a new Tor identity using the `NEWNYM` signal.
4. **Perform Security Checks:** Executes security tools (`nmap`, `nikto`, `socat`) on the specified Onion domain and prints the results.
5. **Terminate Tor Process:** Ends the Tor process after completing the checks.

## from_file.py

The `from_file.py` script extends the functionality of `single.py` by reading multiple Onion domains from a text or CSV file and performing security checks on each. The script follows these steps:

1. **Start Tor Process:** Initializes a Tor process with a specified configuration for `SocksPort` and `ControlPort`.
2. **Authenticate with Tor Controller:** Connects to the Tor control port and authenticates.
3. **Read Domains from File:** Reads a list of Onion domains from a text or CSV file.
4. **Iterate Over Domains:**
   - Requests a new Tor identity for each domain.
   - Executes security tools (`nmap`, `nikto`, `socat`) on each Onion domain and prints the results.
5. **Terminate Tor Process:** Ends the Tor process after processing all domains.

## Possible Automation with These Scripts

These scripts can be used to automate security testing of Onion domains. They demonstrate how to:
- Integrate Tor with security tools.
- Automate the process of changing Tor identities.
- Perform repeated security checks on multiple domains.

Additional tools and tasks that could be automated with similar scripts include:
- Vulnerability scanning with other tools like OpenVAS.
- Web application security testing with OWASP ZAP.
- Network traffic analysis with Wireshark.
- Automated penetration testing with Metasploit.

By leveraging these scripts, various security testing and network analysis tasks can be performed automatically within the Tor network.

#### Credits
**Volkan Sah**
