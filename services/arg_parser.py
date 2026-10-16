import argparse

def get_args():

    parser = argparse.ArgumentParser(
        prog = "pyprobe",
        description="Run port scans",
        epilog="Placeholder"
    )

    parser.add_argument("target")

    parser.add_argument("-J", "--json", action="store_true",help="export discovered ports to a JSON file in the same directory")
    args = parser.parse_args()

    return args.target, args.json