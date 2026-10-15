import requests
import socket
from services.commonly_used_ports import popular_http_ports, popular_services_on_port
from services.common_service_signatures import service_signatures

IP = "127.0.0.1"

def find_service_from_port(IP, PORT):
    if PORT in popular_http_ports:
        try:
            res = requests.get(f"http://{IP}:{PORT}", timeout = 3)
            server_name = res.headers.get("Server", "Unknown HTTP server")
            content_type = res.headers.get("Content-Type", "").split(";")[0]
            
            return f"{server_name} Content: {content_type}"
        except Exception as e:
            return f"HTTP port open but failed to reply. {e}"
    else:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(5)
                sock.connect_ex((IP, PORT)) # Send raw TCP connection with SOCK_STREAM
                banner = sock.recv(1024)

                if not banner:
                    if PORT in popular_services_on_port:
                        return f"Likely {popular_services_on_port[PORT]}"
                    
                    return "Port open but returned no data (silent/filtered)"
                
                for sign in service_signatures:
                    if sign in banner:
                        return service_signatures.get(sign, "unknown")
                
                return banner.decode(errors='ignore')
        except Exception as e:
            return f"unknown Exception: {e}"

def main():
    find_service_from_port("127.0.0.1", 8000)


if __name__ == "__main__":
    main()