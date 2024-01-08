import signal
import time
from datetime import datetime

from helpers import check_python_version
from arguments import check_arguments
from sync import syncroniser

running = True

def signal_handler(sig, frame):
    global running
    print("Log: Ending program")
    running = False

def main():
    signal.signal(signal.SIGINT, signal_handler)
    past = datetime.now()
    present = datetime.now()
    synctime = 0

    check_python_version()
    arguments = check_arguments()
    if not arguments:
        return
    else:
        synctime = int(arguments["sync"])
    print("Log: Initial syncronisation")
    syncroniser(arguments["source"], arguments)
    while(running):
        present = datetime.now()
        diff_time = present - past
        if (diff_time.seconds >= synctime):
            past = present
            syncroniser(arguments["source"], arguments)
        time.sleep(1)

if __name__ == "__main__":
    main()