# Import necessary libraries
import time
import csv
from stem import Signal
from stem.control import Controller
from stem.process import launch_tor_with_config
import subprocess

def start_tor():
    # Start the Tor process with specified configuration
    tor_process = launch_tor_with_config(
        config={
            'SocksPort': '9050',
            'ControlPort': '9051',
        },
        init_msg_handler=lambda line: print(line),
    )
    print("Tor process started")
    return tor_process

def new_tor_identity(controller):
    # Request a new identity for Tor
    controller.signal(Signal.NEWNYM)
    print("New identity requested")

def perform_security_checks(onion_domain):
    # Define the tools and commands to be used for security checks
    tools_commands = {
        'nmap': ['nmap', '-sV', onion_domain],
        'nikto': ['nikto', '-h', onion_domain],
        'socat': ['socat', '-d', '-d', 'TCP4-LISTEN:8080,fork', f'SOCKS4A:127.0.0.1:{onion_domain}:80,socksport=9050'],
    }

    # Execute each tool with the specified command
    for tool, command in tools_commands.items():
        print(f"Running {tool} on {onion_domain}")
        result = subprocess.run(command, capture_output=True, text=True)
        print(f"{tool} output:\n{result.stdout}\n")

def read_domains_from_file(file_path):
    # Read domains from a text or CSV file
    domains = []
    if file_path.endswith('.txt'):
        with open(file_path, 'r') as file:
            domains = [line.strip() for line in file.readlines()]
    elif file_path.endswith('.csv'):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            domains = [row['domain'].strip() for row in reader]
    return domains

def main(file_path):
    tor_process = start_tor()
    time.sleep(10)  # Allow some time for Tor to fully start

    with Controller.from_port(port=9051) as controller:
        controller.authenticate()  # Authenticate with the Tor control port
        
        print("Tor Version:", controller.get_version())
        print("Allowed SocksPort:", controller.get_conf("SocksPort"))
        
        domains = read_domains_from_file(file_path)
        
        # Perform security checks with new Tor identity for each domain
        for onion_domain in domains:
            new_tor_identity(controller)
            perform_security_checks(onion_domain)
            time.sleep(10)  # Wait for Tor to establish new identity

    # Terminate the Tor process
    tor_process.terminate()
    print("Tor process terminated")

if __name__ == "__main__":
    file_path = "domains.txt"  # Replace with the actual path to your text or CSV file
    main(file_path)
