import socket
import os

target = "192.168.1.17"

def scan_port(target, port):
# AF_INET = Address Family: Internet 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # connect via TCP over IPv4
        sock.settimeout(1) # time out after one second
        result = sock.connect_ex((target, port)) # returns error codes instead of an exception

        if result == 0:
            return f"{port}: Open, returned status code {result}"
        else:
            return f"{port}: Closed / Filtered - {os.strerror(result)} with status code {result}"

for port in range(1,1001):
    print(scan_port(target, port))