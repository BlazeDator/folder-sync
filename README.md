<h1>WARNING: </h1>
    <h3>The program will try to delete anything in replica directory thats not on source, be careful with the replica argument</h3>

<h1>Example of usage:</h1>

Arguments:

- Source folder - The folder we'll be syncronising in replica
- Replica folder - An exact copy of the source folder
- Sync time - The ammount of seconds between each syncronisation
- Log file path - The path of a csv file where all operations will be logged

Windows:

    python .\main.py "source" "replica" 1 "log\log.csv"

WSL Ubuntu:

    python3 ./main.py "source" "replica" 1 "log/log.csv"

Closing the program:

    ctrl + c

Running unit tests:

    pytest tests

<h2>Goals:</h2>

- Accept command-line arguments:

    1. source folder path
    2. replica folder path
    3. syncronization interval 
    4. log file path

- Syncronise one-way, the content on replica should match exactly the content on the source folder
- Syncronization should be performed periodically (provided argument for interval)
- File creation/copying/removal operations should be logged to the log file and to the
console output