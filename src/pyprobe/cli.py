import asyncio
import time

from rich import print as rich_print

from .scanner import scan
from .cli_args import get_args
from .output import print_results, save_json
from datetime import datetime

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

def main():
    rich_print(ascii_art)
    current_clock_time = datetime.now().strftime("%H:%M:%S")

    start_time = time.perf_counter()

    target, json_export, timeout, verbose_status = get_args()

    if verbose_status:
        rich_print(f"Starting async port scan against [yellow]{target}[/yellow] at {current_clock_time} with verbose logging. \n")
    else:
        rich_print(f"Starting async port scan against [yellow]{target}[/yellow] at {current_clock_time}\n")

    df = asyncio.run(scan(target,timeout,verbose_status))

    if type(df) == str:
        rich_print(f"[red]{df}[/red]")
    else:
        print_results(df)

    elapsed_time = time.perf_counter() - start_time
    rich_print(f"Completed in {elapsed_time:.3f}s\n")

    if json_export:
        save_json(df)


if __name__ == "__main__":
    main()
