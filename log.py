import os, csv
from datetime import datetime

def log_operations(message: str, path: str, arguments: dict[str, str]):
    log_path = os.path.join(arguments["log_dir"], arguments["log_file"])
    date = datetime.now().isoformat(sep=" ", timespec="seconds")
    print(message, path)
    message = message.removeprefix("Log: ")
    
    prepare_dir_file(arguments)
    if os.path.isfile(log_path):
        try:
            with open(log_path, 'a', newline="\n") as file:
                    writer = csv.writer(file)
                    writer.writerow([date, message, path])
        except PermissionError:
            print("Log: No Permissions ", log_path)

def prepare_dir_file(arguments: dict[str, str]):
    log_dir = arguments["log_dir"]
    path = os.path.join(arguments["log_dir"], arguments["log_file"])

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
            log_operations("Log: Creating dir  ", log_dir, arguments)
        except PermissionError:
            print("Log: No Permissions ", log_dir)
    elif os.path.isfile(log_dir):
        try:
            os.remove(log_dir)
            log_operations("Log: Removing file ", log_dir, arguments)
        except PermissionError:
            print("Log: No Permissions ", log_dir)
    elif os.path.isdir(log_dir):
        if os.path.isdir(path):
            try:
                os.rmdir(path)
                log_operations("Log: Removing dir  ", path, arguments)
            except PermissionError:
                print("Log: No Permissions ", path)
                return
        if not os.path.exists(path):
            with open(path, 'w', newline="\n") as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Operation", "Path"])
            log_operations("Log: Creating file ", path, arguments)