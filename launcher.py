lr = input("Press L to search local files, press R to search remote files ")

# if you input anything else other than l or r, the program will quit

if lr == 'L':
    with open("py/logsearcher-local.py") as fl:
        exec(fl.read())

elif lr == 'l':
    with open("py/logsearcher-local.py") as fl:
        exec(fl.read())

elif lr == 'R':
    with open("py/logsearcher-remote.py") as fr:
        exec(fr.read())

elif lr == 'r':
    with open("py/logsearcher-remote.py") as fr:
        exec(fr.read())