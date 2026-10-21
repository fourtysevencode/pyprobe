import asyncio
from pyprobe.scanner import scan

async def security_audit():
    target_ip = "127.0.0.1"
    print(f"Starting asynchronous scan on {target_ip}...")
    
    # Run the async scan loop natively
    results_df = await scan(target_ip, specific_ports=[7000,8001], syn_scan=True)

    if type(results_df) == str:
        print(f"An error occured: {results_df}")
        return 
    
    if results_df.empty:
        print("No open ports found.")
        return

    print("\nScan Results Summary:")
    print(results_df)
    print(type(results_df))

    # Leverage Pandas to immediately filter out unsafe ports

# Execute the async application
asyncio.run(security_audit())
