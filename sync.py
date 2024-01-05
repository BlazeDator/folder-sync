import sys, os

# When using the os walk, I can go topdown or bottomup by using the topdown flag

#for roots, dirs, files in os.walk(arguments["source"]):
    #print(roots)
    #print(dirs)
    #print(files)
    #print("\n------------------------")

# New approach ? call a function on the main dir, for every dir in the listdir call another
# time the function on that dir, after the recursion going through every dir, do the file operations
# maybe create the dirs before going into the next dir

def syncroniser(arguments: dict):
    explore_path(arguments["source"])

def explore_path(path: str):
    files = os.listdir(path)
    for file in files:
        file = os.path.join(path, file)
        if os.path.isdir(file):
            print("dir: ", file)
            explore_path(os.path.join(path, file))
        elif os.path.isfile(file):
            print("file:", file)