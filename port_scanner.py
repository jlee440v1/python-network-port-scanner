import socket
import sys
import time

if len(sys.argv) != 4:
    print("Usage: python3 port_scanner.py <target> <start_port> <end_port>")
    sys.exit(1)

target = sys.argv[1]

try:
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
except ValueError:
    print("Error: Ports must be numbers.")
    sys.exit(1)

if start_port < 1 or end_port > 65535:
    print("Error: Ports must be between 1 and 65535.")
    sys.exit(1)

if start_port > end_port:
    print("Error: Start port must be less than or equal to end port.")
    sys.exit(1)

try:
    socket.gethostbyname(target)
except socket.gaierror:
    print(f"Error: Could not resolve target '{target}'.")
    sys.exit(1)

open_ports = 0
start_time = time.time()

print(f"\nScanning {target} from port {start_port} to {end_port}...")
print("-" * 60)

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)

    result = sock.connect_ex((target, port))

    if result == 0:
        open_ports += 1

        try:
            service = socket.getservbyport(port, "tcp")
        except OSError:
            service = "Unknown"

        print(f"Port {port:<5} OPEN    Service: {service}")

    sock.close()

end_time = time.time()
scan_time = end_time - start_time

print("-" * 60)
print("Scan complete.")
print(f"Open ports found: {open_ports}")
print(f"Scan time: {scan_time:.2f} seconds")
