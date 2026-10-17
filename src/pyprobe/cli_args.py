import argparse

def get_args():

    parser = argparse.ArgumentParser(
        prog = "pyprobe",
        description="Run port scans",
        epilog="Placeholder"
    )

    parser.add_argument("target")

    parser.add_argument("-j", "--json", action="store_true",help="export discovered ports to a JSON file in the same directory")

    parser.add_argument("-t", "--timeout", type=int, help="set time duration before connection timeouts")
    args = parser.parse_args()

    return args.target, args.json, args.timeout