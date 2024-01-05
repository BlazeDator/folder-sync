from helpers import check_python_version
from arguments import check_arguments
from sync import sync

def main():
    check_python_version()
    arguments = check_arguments()

    if arguments is None:
        return
    sync(arguments)

if __name__ == "__main__":
    main()