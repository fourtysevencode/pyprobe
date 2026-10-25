import asyncio
import pandas as pd

from .services.find_service import find_service_from_port
from .services.scan_port import scan_port
from .services.commonly_used_ports import ports
from .services.syn_scan import syn_scan as ss_scan


async def scan(IP,timeout=3,verbose_status=False,specific_ports: list[int] | None = None,syn_scan=False,):
    if not specific_ports:
        specific_ports = ports

    scanner = ss_scan if syn_scan else scan_port

    tasks = [asyncio.to_thread(scanner,IP,port,timeout,verbose_status,)for port in specific_ports]

    try:
        result = await asyncio.gather(*tasks)
    except PermissionError as e:
        return f"{e}"
    except Exception as e:
        return f"Scan failed: {e}"

    # Keep only valid integer port numbers.
    open_ports = [port for port in result if isinstance(port, int)and not isinstance(port, bool)and 1 <= port <= 65535]

    service_tasks = [asyncio.to_thread(find_service_from_port, IP, port)for port in open_ports]

    try:
        services = await asyncio.gather(*service_tasks)
    except Exception as e:
        return f"Service detection failed: {e}"

    return pd.DataFrame({
        "Port": open_ports,
        "Service": services,
    })
