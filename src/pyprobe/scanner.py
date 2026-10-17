import pandas as pd
from rich import print as rich_print
from datetime import datetime
import asyncio
from .services.find_service import find_service_from_port
from .services.scan_port import scan_port
from .services.commonly_used_ports import ports

ascii_art = r"""
 ________  ___    ___ ________  ________  ________  ________  _______      
|\   __  \|\  \  /  /|\   __  \|\   __  \|\   __  \|\   __  \|\  ___ \     
\ \  \|\  \ \  \/  / | \  \|\  \ \  \|\  \ \  \|\  \ \  \|\ /\ \   __/|    
 \ \   ____\ \    / / \ \   ____\ \   _  _\ \  \\\  \ \   __  \ \  \_|/__  
  \ \  \___|\/   / /   \ \  \___|\ \  \\  \\ \  \\\  \ \  \|\  \ \  \_|\ \ 
   \ \__\ __/   / /     \ \__\    \ \__\\ _\\ \_______\ \_______\ \_______\
    \|__||\____/ /       \|__|     \|__|\|__|\|_______|\|_______|\|_______|
         \|____|/                                                                                                              
"""

async def scan(IP):
    rich_print(ascii_art)
    current_clock_time = datetime.now().strftime("%H:%M:%S")

    rich_print(f"Starting async port scan against [yellow]{IP}[/yellow] at {current_clock_time}\n")

    tasks = [asyncio.to_thread(scan_port,IP,port) for port in ports] # list of tasks to be run asynchronously
    result = await asyncio.gather(*tasks) # fire all tasks

    open_ports = [port for port in result if port is not None]

    service_tasks = [asyncio.to_thread(find_service_from_port, IP, port) for port in open_ports]
    services = await asyncio.gather(*service_tasks)
    
    return pd.DataFrame({"Port":open_ports, "Service":services})