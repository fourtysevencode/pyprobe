import socket

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
        
        target = "127.0.0.1"
        port = 8001
        scan_port(target, port, verbose_status=True)