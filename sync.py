import os, shutil, hashlib

# TODO: Write operations to log file

def syncroniser(source: str, arguments: dict[str, str]):
    entries: list = os.listdir(source)
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
    replica_entries: list = os.listdir(replica)

    for r_entry in replica_entries:
        if r_entry not in entries:
            r_entry = os.path.join(replica, r_entry)
            if os.path.isfile(r_entry):
                print("Log: Removing file ", r_entry)
                os.remove(r_entry)
            elif os.path.isdir(r_entry):
                if len(os.listdir(r_entry)) > 0:
                    sync_cleanup(r_entry, [])
                print("Log: Removing dir ", r_entry)
                os.rmdir(r_entry)

def sync_file(source: str, replica: str):
    if not os.path.exists(replica):
        print("Log: Creating file ", replica)
        shutil.copyfile(source, replica)
    elif os.path.isfile(replica) and files_different(source, replica):
        print("Log: Updating file ", replica)
        shutil.copyfile(source, replica)
    elif os.path.isdir(replica):
        print("Log: Removing dir ", replica)
        os.rmdir(replica)
        print("Log: Creating file ", replica)
        shutil.copyfile(source, replica)

def files_different(source: str, replica: str) -> bool:
    with open(source, "rb") as f:
        file_sha = hashlib.file_digest(f, "sha256").hexdigest()
    with open(replica, "rb") as f:
        replica_sha = hashlib.file_digest(f, "sha256").hexdigest()
    if file_sha != replica_sha:
        return True
    return False

def sync_dir(replica: str):
    if os.path.isdir(replica):
        return
    elif not os.path.exists(replica):
        print("Log: Creating dir ", replica)
        os.mkdir(replica)
    elif os.path.isfile(replica):
        print("Log: Removing file ", replica)
        os.remove(replica)
        print("Log: Creating dir ", replica)
        os.mkdir(replica)