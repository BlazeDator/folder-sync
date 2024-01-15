import hashlib

def files_different(source, replica):
    try:
        with open(source, "rb") as f:
            file_sha = hashlib.file_digest(f, "sha256").hexdigest()
    except PermissionError:
        print("Log: No Permissions ", source)
        return False
    except AttributeError:
        return files_different_alternative(source, replica)
    try:
        with open(replica, "rb") as f:
            replica_sha = hashlib.file_digest(f, "sha256").hexdigest()
    except PermissionError:
        print("Log: No Permissions ", replica)
        return False
    if file_sha != replica_sha:
        return True
    return False

def files_different_alternative(source, replica):    
    file_sha = hashlib.sha256()
    replica_sha = hashlib.sha256()
    chunk = bytes()

    try:
        with open(source,'rb') as f:
            chunk = f.read(1024)
            file_sha.update(chunk)
            while chunk != b'':
                chunk = f.read(1024)
                file_sha.update(chunk)
        file_hash_str = file_sha.hexdigest()
    except PermissionError:
        print("Log: No Permissions ", source)
        return False
    try:
        with open(replica,'rb') as f:
            chunk = f.read(1024)
            replica_sha.update(chunk)
            while chunk != b'':
                chunk = f.read(1024)
                replica_sha.update(chunk)
        replica_hash_str = replica_sha.hexdigest()
    except PermissionError:
        print("Log: No Permissions ", replica)
        return False
    if file_hash_str != replica_hash_str:
        return True
    return False
