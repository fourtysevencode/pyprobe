import socket

target = "192.168.1.17"

def scan_port(target, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((target, port))

    if result == 0:
        print(f"{port}: Open, status code {result}")
        return port

    return None


open_ports = []

for port in range(1, 1001):
    result = scan_port(target, port)

    if result is not None:
        open_ports.append(result)

print("Open ports:", open_ports)