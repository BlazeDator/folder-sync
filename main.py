# System Modules
import sys, os

# Created Modules
from arguments import check_arguments

def main():
    arguments = check_arguments()

    if arguments is None:
        return
    print("Arguments: ", arguments)

if __name__ == "__main__":
    main()