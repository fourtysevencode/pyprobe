import socket
from .commonly_used_ports import ports

target = "127.0.0.1" # ESP32 with a webpage hosted on port 80

def scan_port(target, port,timeout=3,verbose_status=False):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
    
    if result == 0:
        if verbose_status:
            print(f"{port}: Open")
        return port

    return None

if __name__ == "__main__":  
    open_ports = []

    for port in ports:
        result = scan_port(target, port)

        if result is not None:
            open_ports.append(result)

    print("Open ports:", open_ports)