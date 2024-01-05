from helpers import check_python_version
from arguments import check_arguments
from sync import syncroniser

def main():
    check_python_version()
    arguments = check_arguments()

    if not arguments:
        return
    #print(arguments)
    syncroniser(arguments)

if __name__ == "__main__":
    main()