import os
lr = input("[L] to search local files \n[R] to search remote files \n[Q] to quit \n:")

# if you input anything else other than l or r, the program will quit

def clear():
    try:
        os.system('cls')
    except:
        os.system('clear')

if lr == 'L' or lr == 'l':
    clear()
    with open("py/logsearcher-local.py") as fl: exec(fl.read())
elif lr == 'R' or lr == 'r':
    clear()
    with open("py/logsearcher-remote.py") as fl: exec(fl.read())
elif lr =='q' or lr == 'Q': quit()