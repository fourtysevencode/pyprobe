import pandas as pd
from rich import print as rich_print
from datetime import datetime
import asyncio
from .services.find_service import find_service_from_port
from .services.scan_port import scan_port
from .services.commonly_used_ports import ports



async def scan(IP,timeout = 3,verbose_status = False, specific_ports:list[int] = ports):

    if specific_ports is None or len(specific_ports) < 1:
        specific_ports = ports
    
    tasks = [asyncio.to_thread(scan_port,IP,port,timeout,verbose_status) for port in specific_ports] # list of tasks to be run asynchronously

    try:
        result = await asyncio.gather(*tasks) # fire all tasks
    except Exception as e:
        return "An error occured. Provide a valid IPv4 target address."

    open_ports = [port for port in result if port is not None]

    service_tasks = [asyncio.to_thread(find_service_from_port, IP, port) for port in open_ports]
    services = await asyncio.gather(*service_tasks)
    
    return pd.DataFrame({"Port":open_ports, "Service":services})