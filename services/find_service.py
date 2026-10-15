import requests
import socket
from commonly_used_ports import popular_http_ports

IP = "127.0.0.1"

def find_service_from_port(IP, PORT):
    if PORT in popular_http_ports:
        try:
            res = requests.get(f"http://{IP}:{PORT}")
            print(res.text.split()[1])
        except Exception as e:
            print(f"Port {PORT} may not allow HTTP connections.\nException: {e}")
    else:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(5)
                sock.connect_ex((IP, PORT)) # Send raw TCP connection with SOCK_STREAM
                banner = sock.recv(1024).decode()
                print(banner)
        except Exception as e:
            print(f"Port {PORT} may be filtered or closed. Exception: {e}")

def main():
    find_service_from_port("127.0.0.1", 8000)


if __name__ == "__main__":
    main()