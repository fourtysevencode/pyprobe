# Pyprobe

Pyprobe is a command-line tool and Python package for scanning TCP ports, identifying potentially running services, and exporting scan results to JSON. Built from scratch using Python's socket and concurrency capabilities, it aims to make network reconnaissance accessible through both a CLI and a reusable Python API.

## Features

| Feature | Description |
|---|---|
| **Asynchronous Scanning** | Uses `asyncio` and `asyncio.to_thread()` to scan multiple ports concurrently. |
| **TCP Port Scanning** | Identifies accessible TCP ports on a target host. |
| **Service Detection** | Attempts to identify services using port mappings and service signatures. |
| **Terminal Output** | Displays scan results in a formatted table using Rich. |
| **JSON Export** | Saves discovered ports and service information to a JSON file. |
| **CLI and Python API** | Designed for terminal use and integration into Python programs. |

## Installation

Install from PyPI

install it with:

```bash
python -m pip install pyprobe-scan
```

Install from source

Clone the repository:

```bash 
git clone https://github.com/fourtysevencode/pyprobe.git
cd pyprobe
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project in editable mode:

```bash
python -m pip install -e .
```

## Usage

Display help

```bash
pyprobe-scan --help
```

Scan a target

```bash
pyprobe-scan 127.0.0.1
```

Replace 127.0.0.1 with the IP address of a host you own or have explicit permission to test.

Export results to JSON

```bash
pyprobe-scan 127.0.0.1 --json
```

The short form is also available:

```bash
pyprobe-scan 127.0.0.1 -j
```

The scan results are saved to a timestamped JSON file in the current working directory.

Enable verbose logging:

```bash
pyprobe-scan 127.0.0.1 -v
```

Set a timeout on each TCP connection:

```bash
pyprobe-scan 127.0.0.1 -t 3 # Default is 3s
```

### Run directly from source

If you haven't installed the package yet, run it from the repository root:

```bash
PYTHONPATH=src python -m pyprobe 127.0.0.1
```

Using PyProbe in Python

PyProbe is also designed to be imported into your own Python projects.

```python
import asyncio
from pyprobe.scanner import scan

async def main():
    results = await scan("127.0.0.1")
    print(results)

asyncio.run(main())
```

The scanner returns a pandas DataFrame containing discovered ports and their detected service information.

You can process the results using pandas:

```python
results = asyncio.run(scan("127.0.0.1"))

print(results)
print(f"Open ports found: {len(results)}")
```
