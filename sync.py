import os, shutil

from log import log_operations
from files_hash import files_different

def syncroniser(source: str, arguments: dict[str, str]):
    try:
        entries: list = os.listdir(source)
    except PermissionError:
        print("Log: No Permissions ", source)
        return
    replica = source.replace(arguments["source"], arguments["replica"])

    sync_cleanup(replica, entries, arguments)
    for entry in entries:
        entry = os.path.join(source, entry)
        replica = entry.replace(arguments["source"], arguments["replica"])
    
        if os.path.isfile(entry):
            sync_file(entry, replica, arguments)
        elif os.path.isdir(entry):
            next_dir = os.path.join(source, entry)
            sync_dir(replica, arguments)
            syncroniser(next_dir, arguments)

def sync_cleanup(replica: str, entries: list, arguments: dict[str, str]):
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
                    
                except PermissionError:
                    print("Log: No Permissions ", r_entry)
                else:
                    log_operations("Log: Removing file ", r_entry, arguments)
            elif os.path.isdir(r_entry):
                try:
                    if len(os.listdir(r_entry)) > 0:
                        sync_cleanup(r_entry, [], arguments)
                    os.rmdir(r_entry)
                except PermissionError:
                    print("Log: No Permissions ", r_entry)
                else:
                    log_operations("Log: Removing dir  ", r_entry, arguments)
                
def sync_file(source: str, replica: str, arguments: dict[str, str]):
    if not os.path.exists(replica):
        try:
            shutil.copyfile(source, replica)
        except PermissionError:
            print("Log: No Permissions ", source)
            return
        else:
            log_operations("Log: Creating file ", replica, arguments)
    elif os.path.isfile(replica) and files_different(source, replica):
        log_operations("Log: Updating file ", replica, arguments)
        shutil.copyfile(source, replica)
    elif os.path.isdir(replica):
        try:
            os.rmdir(replica)
        except PermissionError:
            print("Log: No Permissions ", replica)
            return
        else:
            log_operations("Log: Removing dir  ", replica, arguments)
        log_operations("Log: Creating file ", replica, arguments)
        shutil.copyfile(source, replica)

def sync_dir(replica: str, arguments: dict[str, str]):
    if os.path.isdir(replica):
        return
    elif not os.path.exists(replica):
        try:
            os.mkdir(replica)
        except:
            print("Log: No Permissions ", replica)
            return
        else:
            log_operations("Log: Creating dir  ", replica, arguments)
    elif os.path.isfile(replica):
        try:
            os.remove(replica)
        except PermissionError:
            print("Log: No Permissions ", replica)
            return
        else:
            log_operations("Log: Removing file ", replica, arguments)
        log_operations("Log: Creating dir  ", replica, arguments)
        os.mkdir(replica)