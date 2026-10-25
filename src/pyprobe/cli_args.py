import argparse

def get_args():

    parser = argparse.ArgumentParser(
        prog = "pyprobe",
        description="Pyprobe is a command-line tool and Python package for scanning TCP ports, identifying potentially running services, and exporting scan results to JSON. Built from scratch using Python's socket and concurrency capabilities, it aims to make network reconnaissance accessible through both a CLI and a reusable Python API.",
        epilog="Placeholder"
    )

    # Arguments
    parser.add_argument("target")

    parser.add_argument("-j", "--json", action="store_true",help="Export discovered ports to a JSON file in the same directory")

    parser.add_argument("-t", "--timeout", type=int, default=3, help="Set time duration before connection timeouts, default is 3s.")

    parser.add_argument("-v", "--verbose", action="store_true", help='Enable verbose logging.')

    parser.add_argument('-p', '--ports', type=int, nargs='+', help='Specific ports to scan')

    parser.add_argument("-sS", "--SYN_SCAN",action="store_true",default=False, help="Use SYN scanning")

    args = parser.parse_args()

    return args.target, args.json, args.timeout, args.verbose, args.ports, args.SYN_SCAN