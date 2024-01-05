import sys, os

def check_arguments() -> dict:
    arguments = {}

    if not check_number_args():
        return None
    if not check_folder_paths():
        return None
    if not check_log_file_path():
        return None
    return arguments

def check_number_args() -> bool:
    if len(sys.argv) != 5:
        print("Error: Wrong number of arguments")
        print("""Usage: python main.py \
<Source folder path> \
<Replica folder path> \
<Sync interval> \
<Log file path>""")
        return False
    return True

def check_folder_paths() -> bool:
    if not os.path.exists(sys.argv[1]):
        print("Error: Invalid source path")
        return False
    if not os.path.exists(sys.argv[2]):
        print("Error: Invalid replica path")
        return False
    return True

def check_log_file_path() -> bool:
    return True