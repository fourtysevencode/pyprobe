import requests
import socket

from services.commonly_used_ports import (popular_http_ports,popular_services_on_port)
from services.common_service_signatures import service_signatures


def find_service_from_port(IP, PORT):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(3)

            result = sock.connect_ex((IP, PORT))

            if result != 0:
                return "Port closed or connection failed"

            # Try to read a banner first
            try:
                banner = sock.recv(1024)
            except socket.timeout:
                banner = b""

        if banner.startswith(b"220") and b"FTP" in banner.upper():
            return "Likely FTP"
        
        if banner:
            for signature, service in service_signatures.items():
                if signature in banner:
                    return service

            return banner.decode("utf-8", errors="ignore").strip()

        # Probe HTTP ports if no banner was received
        try:
            response = requests.get(f"http://{IP}:{PORT}/",timeout=3,)

            server = response.headers.get("Server", "Unknown HTTP server")
            content_type = response.headers.get(
                "Content-Type", ""
            ).split(";")[0]

            return f"HTTP | {server}" # | Content-Type: {content_type}

        except requests.RequestException:
            pass

        # Use the port number as a weak clue
        if PORT in popular_services_on_port:
            return f"Likely: {popular_services_on_port[PORT]}"

        return "Open port, but no banner received"

    except OSError as e:
        return f"Socket error: {e}"


def main():
    result = find_service_from_port("127.0.0.1", 50)
    print(result)


if __name__ == "__main__":
    main()