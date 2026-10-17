import asyncio
import time

from rich import print as rich_print

from .scanner import scan
from .cli_args import get_args
from .output import print_results, save_json


def main():
    start_time = time.perf_counter()

    target, json_export, timeout, verbose_status = get_args()

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
