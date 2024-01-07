import sys

def check_python_version():
    if sys.version_info[0] < 3 \
        or (sys.version_info[0] == 3 and sys.version_info[1] < 12):
            print("Log: Python version older then development version")
            print("Log: Application developed on Python 3.12.1")
            print("Log: hashlib.file_digest was only added on 3.11")
            print("Log: type hinting was added on 3.5")