from services.scan_port import scan_port
from services.find_service import find_service_from_port
from services.commonly_used_ports import ports
from services.arg_parser import get_args
import asyncio
import pandas as pd
import time
from datetime import datetime
from rich import print as rich_print
from rich_tools import df_to_table

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

def main():
    start_time = time.perf_counter()


    target, json_export = get_args()

    df = asyncio.run(scan(target))
    
    table = df_to_table(df)
    total_open_ports = df.shape[0]

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    rich_print(table)
    print(f"\nNumber of ports open: {total_open_ports}")
    print(f"Completed in {elapsed_time:.3f}s\n")

    if json_export:
        file_name = f"PYPROBE-{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.json"
        df.to_json(file_name, indent=4)
        rich_print(f"Saved to [green]{file_name}[/green]")

if __name__ == "__main__":  
    main()