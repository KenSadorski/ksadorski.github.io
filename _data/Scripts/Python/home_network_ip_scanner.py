import os
import subprocess
import socket

def check_ip_address(ip):
    # Ping the IP address to check if it's active
    try:
        response = subprocess.run(['ping', '-n', '1', '-w', '500', ip],
                                  stdout=subprocess.DEVNULL)
        return response.returncode == 0  # True if ping succeeds
    except Exception as e:
        print(f"Error pinging {ip}: {e}")
        return False

def get_hostname(ip):
    try:
        # Attempt to get the hostname
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        # If hostname cannot be resolved, return None
        return None

def scan_network_and_save_results(network_prefix="192.168.50", directory="C:\\temp", filename="192.168.50.1-24_scan_results.txt"):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Full path to save the file
    filepath = os.path.join(directory, filename)
    
    with open(filepath, "w") as file:
        file.write(f"Scan Results for Network {network_prefix}.1/24\n")
        file.write("IP Address        Status      Hostname\n")
        file.write("---------------------------------------------------\n")
        
        # Scan each address in the 192.168.50.1/24 range
        for oct4 in range(1, 256):  # Scans from .1 to .255
            ip_address = f"{network_prefix}.{oct4}"
            is_active = check_ip_address(ip_address)
            if is_active:
                hostname = get_hostname(ip_address) or "Unknown"
                file.write(f"{ip_address:<15} Active      {hostname}\n")
                print(f"{ip_address} is Active - Hostname: {hostname}")
            else:
                file.write(f"{ip_address:<15} Inactive\n")
                print(f"{ip_address} is Inactive")
    
    print(f"\nNetwork scan results saved to {filepath}")

# Call the function to scan the network and save the results
scan_network_and_save_results()
