from services.scan_port import scan_port
from services.find_service import find_service_from_port
from services.commonly_used_ports import ports
from services.arg_parssr import get_target
import asyncio
import pandas as pd

async def scan(IP):
    print(f"Starting async port scan against {IP}")

    tasks = [asyncio.to_thread(scan_port,IP,port) for port in ports] # list of tasks to be run asynchronously
    result = await asyncio.gather(*tasks) # fire all tasks

    open_ports = [port for port in result if port is not None]

    service_tasks = [asyncio.to_thread(find_service_from_port, IP, port) for port in open_ports]
    services = await asyncio.gather(*service_tasks)

    return pd.DataFrame({"Port":open_ports, "Service":services})

def main():
    df = asyncio.run(scan(get_target()))
    print(df)

if __name__ == "__main__":
    main()

# argparse