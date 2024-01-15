import sys, os

def check_arguments():

    if not check_arg_count():
        return {}
    if not check_folder_paths():
        return {}
    if not check_sync_time():
        return {}
    if not check_log_file_path():
        return {}
    arguments = args_to_dict()
    return arguments

def check_arg_count():
    if len(sys.argv) != 5:
        print("Error: Wrong number of arguments")
        print("Usage: python main.py \
<Source folder path> \
<Replica folder path> \
<Sync interval (seconds)> \
<Log file path>")
        return False
    elif (len(sys.argv[1].strip()) < 1):
        print("Error: Invalid source directory")
        return False
    elif (len(sys.argv[2].strip()) < 1):
        print("Error: Invalid replica directory")
        return False
    elif (len(sys.argv[4].strip()) < 1):
        print("Error: Invalid log argument")
        return False
    return True

def check_folder_paths():
    if os.path.abspath(sys.argv[1]) == os.path.abspath(sys.argv[2]):
        print("Error: Source and replica directory are the same")
        return False
    elif os.path.abspath(sys.argv[1]) in  os.path.abspath(sys.argv[2]):
        print("Error: Replica directory inside source, infinite loop")
        return False
    if not os.path.isdir(sys.argv[1]):
        path = os.path.split(os.path.abspath(sys.argv[1]))[0]
        if not os.path.exists(sys.argv[1]) and os.path.isdir(path):
            try:
                os.mkdir(sys.argv[1])
                print("Log: Creating source directory")
            except:
                print("Error: Invalid replica directory")
                return False
        else:
            print("Error: Invalid source directory")
            return False
    if not os.path.isdir(sys.argv[2]):
        path = os.path.split(os.path.abspath(sys.argv[2]))[0]
        if not os.path.exists(sys.argv[2]) and os.path.isdir(path):
            try:
                os.mkdir(sys.argv[2])
                print("Log: Creating replica directory")
            except:
                print("Error: Invalid replica directory")
                return False  
        else:
            print("Error: Invalid replica directory")
            return False
    return True

def check_log_file_path():
    folder = os.path.split(sys.argv[4])[0]
    file = os.path.split(sys.argv[4])[1]

    if not os.path.isdir(folder) and len(os.path.split(folder)[0]) > 0:
        path = os.path.split(os.path.abspath(folder))[0]
        if not os.path.exists(folder) and os.path.isdir(path):
            try:
                os.mkdir(folder)
                print("Log: Creating Log directory")
            except:
                print("Error: Invalid Log directory")
                return False
        else:
            print("Error: Invalid Log directory")
            return False
    elif not file.endswith(".csv") or len(file.split(".csv")[0]) < 1:
        print("Error: Please specify a example.csv file")
        return False
    if not os.path.isfile(sys.argv[4]):
        print("Log: Log file not found, a new one will be created")
    return True

def check_sync_time():
    if not sys.argv[3].isnumeric() or not int(sys.argv[3]) > 0:
        print("Error: Sync time isnt an integer > 0")
        return False
    return True

def args_to_dict():
    arguments = {}
    arguments["source"] = os.path.abspath(sys.argv[1])
    arguments["replica"] = os.path.abspath(sys.argv[2])
    arguments["sync"] = sys.argv[3]
    arguments["log_dir"] = os.path.abspath(os.path.split(sys.argv[4])[0])
    arguments["log_file"] = os.path.split(sys.argv[4])[1]
    return arguments
