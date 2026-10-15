import requests
import socket
from commonly_used_ports import popular_http_ports

IP = "127.0.0.1"

def find_service_from_port(IP, PORT):
    if PORT in popular_http_ports:
        res = requests.get(f"http://{IP}:{PORT}")
        print(res.text.split()[1])
    else:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5)
            sock.connect_ex((IP, PORT)) # Send raw TCP connection with SOCK_STREAM
            banner = sock.recv(1024).decode()
            print(banner)

find_service_from_port("127.0.0.1", 8000)