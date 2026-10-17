from pyprobe.scanner import scan
from pyprobe.cli_args import get_args
import time
from rich import print as rich_print
from rich_tools import df_to_table
import asyncio
from datetime import datetime

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
        file_name = f"PYPROBE-{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.json"
        df.to_json(file_name, orient='records', indent=4)
        rich_print(f"Saved to [green]{file_name}[/green]")

if __name__ == "__main__":  
    main()