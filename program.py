import logging
import os
import signal
from sys import stderr
import sys

from colorama import Fore, Style

from app import app

COLORS = [Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX]


def check_root():
    if os.getuid() != 0:
        stderr.write(f"{COLORS[2]}Error: Please run the script as root!\n")
        exit(-1)


# print a random ascii logo on the screen
def show_ascii_logo():
    cpath = os.getcwd()
    lpath = "/logos/"
    # choose a random logo
    logopath = cpath + lpath + "05.txt"
    # print logo if paths exists
    if os.path.exists(logopath):
        with open(logopath, "r") as f:
            print(COLORS[1] + f.read() + Style.RESET_ALL)
            return None
    # write error to stderr
    stderr.write(f"{COLORS[2]}Error: Logo not found.\n")


def load_commands():
    pass


# no more stack trace when you hit ctrl-c
def handler():
    sys.exit(0)


def start_server():
    signal.signal(signal.SIGINT, handler)
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(debug=True, host="0.0.0.0", port=25565, use_reloader=False)
