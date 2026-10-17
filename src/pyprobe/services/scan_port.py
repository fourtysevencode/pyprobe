import socket
from .commonly_used_ports import ports

target = "127.0.0.1" # ESP32 with a webpage hosted on port 80

def scan_port(target, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(5)
        result = sock.connect_ex((target, port))

    if result == 0:
        #print(f"{port}: Open")
        return port

    return None

if __name__ == "__main__":  
    open_ports = []

    for port in ports:
        result = scan_port(target, port)

        if result is not None:
            open_ports.append(result)

    print("Open ports:", open_ports)