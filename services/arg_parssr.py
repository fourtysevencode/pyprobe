import argparse

def get_target():

    parser = argparse.ArgumentParser(
        prog = "pyprobe",
        description="Run port scans",
        epilog="Placeholder"
    )

    parser.add_argument("target")

    args = parser.parse_args()

    return args.target