# This program is made for searching large log files for errors.
#---------------------------------------------------
# HOW TO USE
#---------------------------------------------------
# 1. when the program asks for a file location, paste in the location of the log file you want to test. if it is an invalid file, the program will quit
# 2. input the search term, eg. the error you want to find
# 3. the program will ask to create a file containing the search hits. if you want to do so, refer to step 3-a
# 3-a. the program will ask for a file name. files are automatically created in .lsoutput, so name the file without an extention. if you want to disable this, check the comment on line 38
# 3-b. the program will ask for a folder in which to save the file. if the folder specified is not available, the program will create one
# 4. the program will find all the instances of that error message in the log file. if there are no instances of the term, you will be prompted to exit
# 5. after the program is finished with finding the instances, it will prompt to exit

# made by alpenstorm

import os
import json

# assigning the global variables
global rootfolder
global indexfolder
global stripfolder
global settings 

global mode
mode = 'debug' # mode controls some prints throughout the program if mode is 'debug', change it to 'release' to turn off the prints ¯\_(ツ)_/¯ 

# pre-run checks
try:
    os.listdir("conf/")
except:
    print('NO CONFIG FOLDER FOUND AT conf/, CREATING...')
    os.mkdir("conf/")

try:
    with open('conf/config.json', 'r') as f:
        settings = json.load(f)
    rootfolder  = settings["rootfolder"]
    indexfolder = settings["indexfolder"]
    stripfolder = settings["stripfolder"]
except:
    print('NO CONFIG FILE FOUND AT "conf/config.json, CREATING...')
    data = {"rootfolder": "root/", "indexfolder": "index/", "stripfolder": "stripped/"}
    with open('conf/config.json', "w") as w:
        w.write(json.dumps(data, indent=4))
    with open('conf/config.json', 'r') as r:
        settings = json.load(r)

    rootfolder  = settings["rootfolder"]
    indexfolder = settings["indexfolder"]
    stripfolder = settings["stripfolder"]


try:
    os.listdir(rootfolder)
    os.listdir(rootfolder+indexfolder)
    os.listdir(rootfolder+stripfolder)
except:
    print(f"NO ROOT FOLDER FOUND AT {rootfolder}, CREATING...")
    os.mkdir(rootfolder)
    print(f"NO INDEX FOLDER FOUND AT {indexfolder}, CREATING...")
    os.mkdir(rootfolder+indexfolder)
    print(f"NO STRIP FOLDER FOUND AT {stripfolder}, CREATING...")
    os.mkdir(rootfolder+stripfolder)

# functions
def clear():
    try:
        os.system('cls')
    except:
        os.system('clear')

def inputFile(): 
    global fn
    fn = input("Enter File Location: ")
    clear()

def options():
    ops = input("[A] to add or change a file (do this before searching, reading, or editing to avoid NO FILE errors) \n[S] to search the file \n[R] to read the file \n[RS] to refresh settings (do this after changing the save folder for indexes and strips) \n[E] to edit the file \n[B] to go back \n[Q] to quit \n:")

    if ops == "r" or ops == "R": 
        clear()
        read()
    elif ops == "s" or ops == "S":
        clear()
        beforeSearch()
    elif ops == "e" or ops == "E":
        clear()
        edit()
    elif ops == "a" or ops == "A":
        clear()
        inputFile()
        options()
    elif ops == "b" or ops == "B":
        clear()
        try: 
            with open("launcher.py") as orig: exec(orig.read())
        except: 
            with open("../launcher.py") as orig: exec(orig.read())
    elif ops == "rs" or ops == "RS" or ops == "rS" or ops == "Rs":
        clear()
        try: 
            with open("py/logsearcher-local.py") as orig: exec(orig.read())
        except: 
            with open("logsearcher-local.py") as orig: exec(orig.read())   
    elif ops == "q" or ops == "Q": quit()

def edit():

    try:
        print(f"Current File: {fn.split('/', 1)[1]}")
    except:
        print(f"Current File: {fn}")

        
    ops = input("[V] to use Vim (if installed) \n[NV] to use Neovim (if installed) \n[N] to use Notepad (if using Windows) \n[C] to use VS Code (if installed) \n[B] to go back \n:")
    if ops == "v" or ops == "V": 
        os.system('vim ' + fn)
        clear()
        edit()
    elif ops == "nv" or ops == "NV" or ops == "Nv" or ops == "nV":
        os.system('nvim ' + fn)
        clear()
        edit()
    elif ops == "n" or ops == "N": 
        os.system('notepad ' + fn)
        clear()
        edit()
    elif ops == "c" or ops == "C":
        os.ystem('code ' + fn)
        clear()
        edit()
    elif ops == "b" or ops == "B":
        clear()
        options()

def changeFolder():
    rootfolder  = str(input("Enter Location for Root folder ([I] for info): "))
    if rootfolder == "i" or rootfolder == "I":
        print('''LogSearcher uses a simple folder structure for storing index and strip files:             
                          
        LogSearcher Root Folder (containing launcher.py)
                        |
                        |
                        |
                    root (root folder)
                        |
                        |
                        |
                        |
                        |-- index (storing the index files)
                        |        |
                        |        |
                        |        |-- something-index.json (all index files are in JSON format
                        |                                  and have the original file name - 
                        |                                  index)         
                        |
                        |
                        |
                        |-- stripped (storing the stripped versions of the logs)
                        |        |
                        |        |
                        |        |-- something-strip.log (strip files are in the original format)
                 
                 when creating custom folders from the program, always use "foldername/" instead of "foldername
                 please keep this basic folder structure or some things might break!!! if they do, delete
                 "conf/" and "root/" to rebuild them''') 
        
        bck = input("\n\n\n[B] to go back \n:")
        if bck == "b" or bck == "B":
            clear()
            changeFolder()
    indexfolder = rootfolder + str(input('Enter Location for Index folder ("indexfolder/"): '))
    stripfolder = rootfolder + str(input('Enter Location for Strip folder ("stripfolder/"): '))
    
    try:
        os.listdir(rootfolder)
        os.listdir(rootfolder+indexfolder)
        os.listdir(rootfolder+stripfolder)
    except:
        print(f"NO ROOT FOLDER FOUND AT {rootfolder}, CREATING...")
        os.mkdir(rootfolder)
        print(f"NO INDEX FOLDER FOUND AT {indexfolder}, CREATING...")
        os.mkdir(indexfolder)
        print(f"NO STRIP FOLDER FOUND AT {stripfolder}, CREATING...")
        os.mkdir(stripfolder)

    data = {"rootfolder": rootfolder, "indexfolder": indexfolder.split('/', 1)[1], "stripfolder": stripfolder.split('/', 1)[1]}
    with open('conf/config.json', "w") as f:
        f.write(json.dumps(data, indent=4))
    
    input('Successfully wrote to conf/config.json, press [ENTER] to refresh settings')

    clear()
    try: 
        with open("py/logsearcher-local.py") as orig: exec(orig.read())
    except: 
        with open("logsearcher-local.py") as orig: exec(orig.read())  


def indexFile(input_file: str, output_file: str):
    
    try:
        open(input_file, "r")
    except:
        xt = input("Error, file not found. \nTry again? [Y,N] \n:")

        if xt == "Y" or xt == "y": 
            clear()
            inputFile()
            indexFile()
        elif xt == "n" or xt == "N": readActions()
    
    counts = {}
    with open(input_file, "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                #word = word.lower() #we might not want to lowercase all the words!
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
  
    sorted_list = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = {k: v for k, v in sorted_list}
    with open(output_file, "w") as f:
        f.write(json.dumps(sorted_dict, indent=4))

def stripWhiteSpace(input_file: str, output_file: str):
    
    try:
        open(input_file, "r")
    except:
        xt = input("Error, file not found. \nTry again? [Y,N] \n:")

        if xt == "Y" or xt == "y": 
            clear()
            inputFile()
            indexFile()
        elif xt == "n" or xt == "N": readActions()

    with open(input_file, "r") as f:
        content = f.read().replace(" ", "").replace("\n", "")
    with open(output_file, "w") as f:
        f.write(content)

def readActions():
    xt = input("[I] to index this file \n[W] to strip white space in this file \n[C] to change root folder \n[B] to go back \n:")

    try:
        localfn = fn.split('/', 1)[1]
    except:
        localfn = fn


    if xt == "i" or xt == "I": 
        clear()
        indexFile(fn, f"{rootfolder}{indexfolder}" + f"{localfn.split('.', 1)[0]}-index.json")
    elif xt == "w" or xt == "W":
        clear()
        stripWhiteSpace(fn, f"{rootfolder}{stripfolder}" + f"{localfn.split('.', 1)[0]}-strip.{localfn.split('.', 1)[1]}")
    elif xt == "c" or xt == "C":
        clear()
        changeFolder()
    elif xt == "b" or xt == "B":
        clear()
        options()

def read():
    
    try:
        print(f"Current File: {fn.split('/', 1)[1]}")
    except:
        print(f"Current File: {fn}")

    readActions()
    
    try:
        fileHandle = open(fn, "r", encoding="utf8", errors="ignore") 
    except:
        xt = input("Error, file not found. \nTry again? [Y,N] \n:")

        if xt == "Y" or xt == "y": 
            clear()
            inputFile()
            read()
        elif xt == "n" or xt == "N": options()
    
    lc = 0

    for line in fileHandle:
        line = line.rstrip()
        lc += 1
        print(line + "    AT: LINE " + str(lc))
    
    xt = input("[RN] to read a new file \n[B] to go back \n:")
    if xt == "RN" or xt == "rn" or xt == "Rn" or xt == "rN": 
        clear()
        inputFile()
        read()
    elif xt == "b" or xt == "B":
        clear()
        options()

def beforeSearch():
    try:
        print(f"Current File: {fn.split('/', 1)[1]}")
    except:
        print(f"Current File: {fn}")

    q = input("Is this a regular file or an index? [R,I] \n[C] to change file \n:")

    if q == "i" or q == "I": 
        clear()
        searchIndex()
    elif q == "r" or q == "R": 
        clear()
        search()
    elif q == "c" or q == "C":
        clear()
        inputFile()
        beforeSearch()
    elif q == "b" or q == "B":
        clear()
        options()    

def searchIndex():
    try:
        with open(fn, "r", encoding="utf8", errors="ignore") as fileHandle:
            data = json.load(fileHandle)
    except:
        xt = input("Error, file not found. \nTry again? [Y,N] \n:")

        if xt == "Y" or xt == "y": 
            clear()
            inputFile()
            search()
        elif xt == "n" or xt == "N": options()

    trm = input("Enter Search Term: ")

    clear()
    
    print(f"Found " + str(data[f"{trm}"]) + f" instances of {trm} in {fn.split('/', 1)[1]}")

    xt = input("[S] to search again with the same file name \n[SN] to search again with a new file name \n[B] to go back \n:")

    if xt == "s" or xt == "S": 
        clear()
        search()
    elif xt == "SN" or xt == "sn" or xt == "Sn" or xt == "sN": 
        clear()
        inputFile()
        search()
    elif xt == "b" or xt == "B":
        clear()
        options()

def search():
    try:
        fileHandle = open(fn, "r", encoding="utf8", errors="ignore") 
    except:
        xt = input("Error, file not found. \nTry again? [Y,N] \n:")

        if xt == "Y" or xt == "y": 
            clear()
            inputFile()
            search()
        elif xt == "n" or xt == "N": quit()

    trm = input("Enter Search Term: ")

    tc = 0
    lc = 0

    flcr = input("Create a File? y/n ")

    if flcr == 'y':
        print("WARNING: FILES WILL OVERWRITE IF THEY HAVE THE SAME NAME")
        filen = input("File Name: ")
        foldern = input("File Location: ")

        try:
            with open(foldern + filen, "w") as output: #if you want to change the file format that the program exports to, define it here instead of ".lsout". 
                output.write("------OUTPUT FILE CREATED------"+ "\n\n")

                for line in fileHandle:
                    line = line.rstrip()
                    lc += 1
                    if not trm in line:
                        continue
                    tc += 1
                    output.write(line + "\n\n")
                    print(line + "    AT: LINE " + str(lc))
            
                output.write("------OUTPUT FILE TERMINATED------")
            
                print("\nFound", tc, "terms \nIn", lc, "lines \nFrom location", fn, "\n")
                
                xt = input("[S] to search again with the same file name \n[SN] to search again with a new file name \n[B] to go back \n:")

                if xt == "s" or xt == "S": 
                    clear()
                    search()
                elif xt == "SN" or xt == "sn" or xt == "Sn" or xt == "sN": 
                    clear()
                    inputFile()
                    search()
                elif xt == "b" or xt == "B":
                    clear()
                    options()
                
        except:
            os.mkdir(foldern)

            with open(foldern + filen, "w") as output:
                output.write("------OUTPUT FILE CREATED------"+ "\n\n")

                for line in fileHandle:
                    line = line.rstrip()
                    lc += 1
                    if not trm in line:
                        continue
                    tc += 1
                    output.write(line + "\n\n")
                    print(line + "    AT: LINE " + str(lc))
            
                output.write("------OUTPUT FILE TERMINATED------")
            
                print("\nFound", tc, "terms \nIn", lc, "lines \nFrom location", fn, "\n")

                xt = input("[S] to search again with the same file name \n[SN] to search again with a new file name \n[B] to go back \n:")

                if xt == "s" or xt == "S": 
                    clear()
                    search()
                elif xt == "SN" or xt == "sn" or xt == "Sn" or xt == "sN": 
                    clear()
                    inputFile()
                    search()
                elif xt == "b" or xt == "B":
                    clear()
                    options()
    
    for line in fileHandle:
        line = line.rstrip()
        lc += 1
        if not str(trm) in line: 
            continue
        tc += 1
        print(str(line) + "    AT: LINE " + str(lc))


    print("\nFound", tc, "terms \nIn", lc, "lines \nFrom location", fn, "\n")


    xt = input("[S] to search again with the same file name \n[SN] to search again with a new file name \n[B] to go back \n:")

    if xt == "s" or xt == "S": 
        clear()
        search()
    elif xt == "SN" or xt == "sn" or xt == "Sn" or xt == "sN": 
        clear()
        inputFile()
        search()
    elif xt == "b" or xt == "B":
        clear()
        options()

# start the program
fn = "empty"
options()