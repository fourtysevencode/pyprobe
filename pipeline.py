from services.scan_port import scan_port
from services.find_service import find_service_from_port
from services.commonly_used_ports import ports
import pandas as pd

def scan(IP):
    open_ports = []
    for port in ports:
        res = scan_port(IP, port)
        if res is not None:
            open_ports.append(res)

    services = [find_service_from_port(IP, port) for port in open_ports]

    result = dict(zip(open_ports, services))

    return pd.DataFrame({"Port":open_ports, "Service":services})

print(scan("fourtysevencode.hackclub.app"))

