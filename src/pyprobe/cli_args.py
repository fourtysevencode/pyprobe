import argparse

def get_args():

    parser = argparse.ArgumentParser(
        prog = "pyprobe",
        description="Run port scans",
        epilog="Placeholder"
    )

    parser.add_argument("target")

    parser.add_argument("-j", "--json", action="store_true",help="Export discovered ports to a JSON file in the same directory")

    parser.add_argument("-t", "--timeout", type=int, help="Set time duration before connection timeouts, default is 3s.")

    parser.add_argument("-v", "--verbose", action="store_true", help='Enable verbose logging.')
    args = parser.parse_args()

    return args.target, args.json, args.timeout, args.verbose