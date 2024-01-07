import os, shutil, hashlib

# TODO: Write operations to log file

def syncroniser(source: str, arguments: dict[str, str]):
    try:
        entries: list = os.listdir(source)
    except PermissionError:
        print("Log: No Permissions ", source)
        return
    replica = source.replace(arguments["source"], arguments["replica"])

    sync_cleanup(replica, entries)
    for entry in entries:
        entry = os.path.join(source, entry)
        replica = entry.replace(arguments["source"], arguments["replica"])
    
        if os.path.isfile(entry):
            sync_file(entry, replica)
        elif os.path.isdir(entry):
            next_dir = os.path.join(source, entry)
            sync_dir(replica)
            syncroniser(next_dir, arguments)

def sync_cleanup(replica: str, entries: list):
    if not os.path.exists(replica):
        return
    try:
        replica_entries: list = os.listdir(replica)
    except PermissionError:
        print("Log: No Permissions ", replica)
        return

    for r_entry in replica_entries:
        if r_entry not in entries:
            r_entry = os.path.join(replica, r_entry)
            if os.path.isfile(r_entry):
                try:
                    os.remove(r_entry)
                    print("Log: Removing file ", r_entry)
                except PermissionError:
                    print("Log: No Permissions ", r_entry)
            elif os.path.isdir(r_entry):
                try:
                    if len(os.listdir(r_entry)) > 0:
                        sync_cleanup(r_entry, [])
                    os.rmdir(r_entry)
                    print("Log: Removing dir ", r_entry)
                except PermissionError:
                    print("Log: No Permissions ", r_entry)
                

def sync_file(source: str, replica: str):
    if not os.path.exists(replica):
        try:
            shutil.copyfile(source, replica)
            print("Log: Creating file ", replica)
        except PermissionError:
            print("Log: No Permissions ", source)
            return
    elif os.path.isfile(replica) and files_different(source, replica):
        print("Log: Updating file ", replica)
        shutil.copyfile(source, replica)
    elif os.path.isdir(replica):
        try:
            os.rmdir(replica)
            print("Log: Removing dir ", replica)
        except PermissionError:
            print("Log: No Permissions ", replica)
            return
        print("Log: Creating file ", replica)
        shutil.copyfile(source, replica)

def files_different(source: str, replica: str) -> bool:
    try:
        with open(source, "rb") as f:
            file_sha = hashlib.file_digest(f, "sha256").hexdigest()
    except PermissionError:
        print("Log: No Permissions ", source)
        return False
    try:
        with open(replica, "rb") as f:
            replica_sha = hashlib.file_digest(f, "sha256").hexdigest()
    except PermissionError:
        print("Log: No Permissions ", replica)
        return False
    if file_sha != replica_sha:
        return True
    return False

def sync_dir(replica: str):
    if os.path.isdir(replica):
        return
    elif not os.path.exists(replica):
        try:
            os.mkdir(replica)
            print("Log: Creating dir ", replica)
        except:
            print("Log: No Permissions ", replica)
            return
    elif os.path.isfile(replica):
        try:
            os.remove(replica)
            print("Log: Removing file ", replica)
        except PermissionError:
            print("Log: No Permissions ", replica)
            return
        print("Log: Creating dir ", replica)
        os.mkdir(replica)