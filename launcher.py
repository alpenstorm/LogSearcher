lr = input("Press L to search local files, press R to search remote files ")

# if you input anything else other than l or r, the program will quit

if lr == 'L':
    with open("py/logsearcher-local.py") as fl:
        print("LOCAL SEARCHER LAUNCHED")
        exec(fl.read())
if lr == 'l':
    with open("py/logsearcher-local.py") as fl:
        print("LOCAL SEARCHER LAUNCHED")
        exec(fl.read())
if lr == 'R':
    with open("py/logsearcher-remote.py") as fl:
        print("REMOTE SEARCHER LAUNCHED")
        exec(fl.read())
if lr == 'r':
    with open("py/logsearcher-remote.py") as fl:
        print("REMOTE SEARCHER LAUNCHED")
        exec(fl.read())