import sys, os

# When using the os walk, I can go topdown or bottomup by using the topdown flag

def files_sync(arguments):
    for roots, dirs, files in os.walk(arguments["source"]):
        print(roots)
        print(dirs)
        print(files)
        print("\n------------------------")
    