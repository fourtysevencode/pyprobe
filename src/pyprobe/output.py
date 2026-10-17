
import json
from pathlib import Path
from datetime import datetime

from rich import print as rich_print
from rich_tools import df_to_table


def print_results(df):
    """Display scan results in a formatted table."""
    rich_print(df_to_table(df))
    rich_print(f"\nNumber of ports open: {df.shape[0]}")


def save_json(df):
    """Export scan results to a JSON file."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"PYPROBE-{timestamp}.json"

    df.to_json(file_name, orient="records", indent=4)

    rich_print(f"Saved to [green]{file_name}[/green]")
    return Path(file_name)
