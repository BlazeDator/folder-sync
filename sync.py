import os, shutil, hashlib

# TODO: Remove files not present on source from replica
# TODO: Separate explore_path function into smaller bits, improve readability
# TODO: Write operations to log file

def syncroniser(arguments: dict[str, str]):
    explore_path(arguments["source"], arguments)

def explore_path(path: str, arguments: dict[str, str]):
    files = os.listdir(path)

    for file in files:
        filesha: str = ""
        replicasha: str = ""
        file = os.path.join(path, file)
        replica = file.replace(arguments["source"], arguments["replica"])

        if os.path.isdir(file):
            if not os.path.exists(replica):
                print("Log: Creating dir ", replica)
                os.mkdir(replica)
            elif os.path.isfile(replica):
                print("Log: Removing file ", replica)
                os.remove(replica)
                print("Log: Creating dir")
                os.mkdir(replica)
            explore_path(os.path.join(path, file), arguments)
        elif os.path.isfile(file):
            with open(file, "rb") as f:
                filesha = hashlib.file_digest(f, "sha256").hexdigest()
            if os.path.isfile(replica):
                with open(replica, "rb") as f:
                    replicasha = hashlib.file_digest(f, "sha256").hexdigest()
            if not os.path.exists(replica):
                print("Log: Creating file ", replica)
                shutil.copyfile(file, replica)
            elif os.path.isfile(replica) and filesha != replicasha:
                print("Log: Updating file ", replica)
                shutil.copyfile(file, replica)
            elif os.path.isdir(replica):
                print("Log: Removing dir ", replica)
                os.rmdir(replica)
                print("Log: Creating file ", replica)
                shutil.copyfile(file, replica)
        