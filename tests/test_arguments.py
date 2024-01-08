import sys, os
from unittest.mock import patch

from arguments \
import \
check_arguments, \
check_arg_count, \
check_folder_paths, \
check_log_file_path, \
check_sync_time, \
args_to_dict

if (os.path.sep == "\\"):
    log = "log\\log.csv"
    log_txt = "log\\log.txt"
elif (os.path.sep == "/"):
    log = "log/log.csv"
    log_txt = "log/log.txt"

def test_check_arguments():
    test_args = ["main.py", "source", "replica", "1" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_arguments() == { \
                                        "source" : os.path.abspath(test_args[1]), \
                                        "replica" : os.path.abspath(test_args[2]), \
                                        "sync" : test_args[3], \
                                        "log_dir" : os.path.abspath(os.path.split(sys.argv[4])[0]), \
                                        "log_file" : os.path.split(sys.argv[4])[1]
                                    }
    test_args = ["main.py", "source", "replica", "2" , log_txt]
    with patch.object(sys, 'argv', test_args):
        assert check_arguments() == {}
    test_args = ["main.py", "source", "replica", "a" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_arguments() == {}
    test_args = ["main.py", "source", "", "1" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_arguments() == {}
    test_args = ["main.py", " ", "replica", "1" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_arguments() == {}
    test_args = ["main.py", "source", "replica", "1" , " "]
    with patch.object(sys, 'argv', test_args):
        assert check_arguments() == {}
    test_args = ["main.py", "source", "replica", "1" , "a"]
    with patch.object(sys, 'argv', test_args):
        assert check_arguments() == {}

def test_check_arg_count():
    test_args = ["main.py", "source", "replica", "1" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_arg_count() == True
    test_args = ["main.py", "", "replica", "1" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_arg_count() == False
    test_args = ["main.py", "source", " ", "1" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_arg_count() == False
    test_args = ["main.py"]
    with patch.object(sys, 'argv', test_args):
        assert check_arg_count() == False
    test_args = ["main.py", "source", "replica", "1" , log, "testing"]
    with patch.object(sys, 'argv', test_args):
        assert check_arg_count() == False
    test_args = ["main.py", "source", "replica", "1" ]
    with patch.object(sys, 'argv', test_args):
        assert check_arg_count() == False

def test_check_folder_paths():
    test_args = ["main.py", "source", "replica", "1" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_folder_paths() == True
    test_args = ["main.py", "source", "source", "1" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_folder_paths() == False
    test_args = ["main.py", "source", "source" + os.path.sep + "replica" , "1" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_folder_paths() == False
    test_args = ["main.py", "", "replica", "1" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_folder_paths() == False
    test_args = ["main.py", "source", "", "1" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_folder_paths() == False

def test_check_log_file_path():
    test_args = ["main.py", "source", "replica", "1" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_log_file_path() == True
    test_args = ["main.py", "source", "replica", "1" , "log.csv"]
    with patch.object(sys, 'argv', test_args):
        assert check_log_file_path() == True
    test_args = ["main.py", "source", "replica", "1" , log_txt]
    with patch.object(sys, 'argv', test_args):
        assert check_log_file_path() == False


def test_check_sync_time():
    test_args = ["main.py", "source", "replica", "1" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_sync_time() == True
    test_args = ["main.py", "source", "replica", "a" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_sync_time() == False
    test_args = ["main.py", "source", "replica", "" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_sync_time() == False
    test_args = ["main.py", "source", "replica", " " , log]
    with patch.object(sys, 'argv', test_args):
        assert check_sync_time() == False
    test_args = ["main.py", "source", "replica", "+-2" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_sync_time() == False
    test_args = ["main.py", "source", "replica", "+2" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_sync_time() == False
    test_args = ["main.py", "source", "replica", "2.5" , log]
    with patch.object(sys, 'argv', test_args):
        assert check_sync_time() == False

def test_args_to_dict():
    test_args = ["main.py", "source", "replica", "1" , log]
    with patch.object(sys, 'argv', test_args):
        assert args_to_dict() == { \
                                        "source" : os.path.abspath(test_args[1]), \
                                        "replica" : os.path.abspath(test_args[2]), \
                                        "sync" : test_args[3], \
                                        "log_dir" : os.path.abspath(os.path.split(sys.argv[4])[0]), \
                                        "log_file" : os.path.split(sys.argv[4])[1]
                                    }