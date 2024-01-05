import sys, os

def check_arguments() -> dict:
    arguments = {}

    if not check_arg_count():
        return None
    if not check_folder_paths():
        return None
    if not check_sync_time():
        return None
    if not check_log_file_path():
        return None
    arguments = args_to_dict()
    return arguments

def check_arg_count() -> bool:
    if len(sys.argv) != 5:
        print("Error: Wrong number of arguments")
        print("Usage: python main.py \
<Source folder path> \
<Replica folder path> \
<Sync interval (seconds)> \
<Log file path>")
        return False
    return True

def check_folder_paths() -> bool:
    if not os.path.isdir(sys.argv[1]):
        print("Error: Invalid source path")
        return False
    elif not os.path.isdir(sys.argv[2]):
        print("Error: Invalid replica path")
        return False
    elif sys.argv[1] == sys.argv[2]:
        print("Error: Source and replica directory are the same")
        return False
    return True

def check_log_file_path() -> bool:
    folder = os.path.split(sys.argv[4])[0]
    file = os.path.split(sys.argv[4])[1]

    if not os.path.isdir(folder):
        print("Error: Log file directory not found")
        return False
    elif not file.endswith(".csv") or len(file.split(".csv")[0]) < 1:
        print("Error: Please specify a example.csv file")
        return False
    if not os.path.isfile(sys.argv[4]):
        print("Log: File not found, a new one will be created")
    return True

def check_sync_time() -> bool:
    if not sys.argv[3].isnumeric() or not int(sys.argv[3]) > 0:
        print("Error: Sync time isnt an integer > 0")
        return False
    return True

def args_to_dict() -> dict:
    arguments = {}
    arguments["source"] = sys.argv[1]
    arguments["replica"] = sys.argv[2]
    arguments["sync"] = int(sys.argv[3])
    arguments["log_dir"] = os.path.split(sys.argv[4])[0]
    arguments["log_file"] = os.path.split(sys.argv[4])[1]
    return arguments