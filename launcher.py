lr = input("Press L to search local files, press R to search remote files ")

# if you input anything else other than l or r, the program will quit

if lr == 'L':
    try:
        with open("py/logsearcher-local.py") as fl:
            print("LOCAL SEARCHER LAUNCHED")
            exec(fl.read())
    except:
        print("Local searcher not found, please consult readme!")
        input("Press [Enter] to exit")

elif lr == 'l':
    try:
        with open("py/logsearcher-local.py") as fl:
            print("LOCAL SEARCHER LAUNCHED")
            exec(fl.read())
    except:
        print("Local searcher not found, please consult readme!")
        input("Press [Enter] to exit")

elif lr == 'R':
    try:
        with open("py/logsearcher-remote.py") as fl:
            print("REMOTE SEARCHER LAUNCHED")
            exec(fl.read())
    except:
        print("Local searcher not found, please consult readme!")
        input("Press [Enter] to exit")

elif lr == 'r':
    try:
        with open("py/logsearcher-remote.py") as fl:
            print("REMOTE SEARCHER LAUNCHED")
            exec(fl.read())
    except:
        print("Local searcher not found, please consult readme!")
        input("Press [Enter] to exit")
