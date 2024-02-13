# LogSearcher is a program that searches large log files
# it can also index files, strip white space, etc.
# i've written explanations for the functions in the comments in the file 

# cheers and happy searching, alpenstorm

import os
import json

# assigning the global variables
global rootfolder
global indexfolder
global stripfolder
global settings  

#---------------------------------------------------
# Pre-run checks
#---------------------------------------------------

# there are three pairs of try-excepts for the checks
# the first one (under this comment) checks if the "conf/" folder exists. if it doesn't, it will create one (conf is where we store the config file)
try:
    os.listdir("conf/")
except:
    print('NO CONFIG FOLDER FOUND AT conf/, CREATING...')
    os.mkdir("conf/")

# this one checks if the config file exists. if it doesn't, it will create one
try:
    with open('conf/config.json', 'r') as f:
        settings = json.load(f)
    rootfolder  = settings["rootfolder"]
    indexfolder = settings["indexfolder"]
    stripfolder = settings["stripfolder"]
    f.close()
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
    w.close()
    r.close()

# and this one checks if the root folders exist
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

#---------------------------------------------------
# Functions
#---------------------------------------------------
    
# the clear function clears the terminal when called
def clear():
    try:
        os.system('cls')
    except:
        os.system('clear')

# the inputFile function asks for a file (fn) and checks if it exists
def inputFile() -> str: 
    global fn
    global fileHandle
    fn = input("Enter File Location: ")

    try:
        fileHandle = open(fn, "r", encoding="utf8", errors="ignore") 
    except:
        xt = input("Error, file not found. \nTry again? [Y,N] \n:")

        if xt == "Y" or xt == "y": 
            clear()
            inputFile()
            read()
        elif xt == "n" or xt == "N": options()
    
    clear()

# the options function shows an options menu that starts the program. from there, you can access everything else
def options():
    ops = input("[A] to add or change a file (do this before searching, reading, or editing to avoid NO FILE errors) \n[S] to search the file \n[R] to read the file \n[C] to change root folder for indexes and strips \n[E] to edit the file \n[B] to go back \n[Q] to quit \n:")

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
    elif ops == "c" or ops == "C":
        clear()
        changeFolder()
    elif ops == "q" or ops == "Q": quit()

# the edit function opens a menu from which you can select an editor to open the current file (fn)
def edit():

    print(f"Current File: {os.path.basename(fn)}")

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

# the changeFolder function lets you change the output folder for the index and strip files
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

# the indexFile function takes two strings (input_file and output_file). it indexes input_file and exports a json output_file with the words in the file and how many there are to root/index
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

# the stripWhiteSpace function takes two strings (input_file and output_file). it strips the white space from input_file and exports a text file (the same format as the input_file) into root/stripped
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

# the clean function takes two strings (input_file and output_file). it cleans up the json that you indexed exports the new one to root/index
def clean(input_file: str, output_file: str):    
    xt = input("Do you want to remove underscores and dashes? [Y,N] \n:")

    if xt == 'y' or 'Y':
        with open(input_file, "r") as f_in:
            with open(output_file, "w") as f_out:
                f_out.write("{")
                for line in f_in:
                    line = "".join(c for c in line if c not in "{}[]/|_-`~;<>^()")
                    f_out.write(line)
                f_out.write("}")
    elif xt == 'n' or 'N':
        with open(input_file, "r") as f_in:
            with open(output_file, "w") as f_out:
                f_out.write("{")
                for line in f_in:
                    line = "".join(c for c in line if c not in "{}[]/|`~;<>^()")
                    f_out.write(line)
                f_out.write("}")

    with open(output_file, "r") as f:
        data = json.load(f)

    unique_data = {}

    for key, value in data.items():
        if key not in unique_data:
            unique_data[key] = value

    sorted_list = sorted(unique_data.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = {k: v for k, v in sorted_list}

    with open(output_file, "w") as f:
        json.dump(sorted_dict, f, indent=4)

# the indexMenu function is an options menu for indexing
def indexMenu():
    xt = input("[I] to index the file regularly \n[C] to clean an existing index file \n[B] to go back \n:")

    localfn = os.path.basename(fn)

    if xt == "i" or xt == "I": 
        clear()
        indexFile(fn, f"{rootfolder}{indexfolder}" + f"{localfn.split('.', 1)[0]}-index.json")
    elif xt == "c" or xt == "C":
        clear()
        clean(fn, f"{rootfolder}{indexfolder}" + f"{localfn.split('.', 1)[0]}-clean.json")
    elif xt == "b" or xt == "B":
        clear()
        readActions()

# the readActions function is an options menu for indexing and stripping files
def readActions():
    xt = input("[I] to index this file \n[W] to strip white space in this file \n[B] to go back \n:")

    localfn = os.path.basename(fn)
    
    if xt == "i" or xt == "I": 
        clear()
        indexMenu()
    elif xt == "w" or xt == "W":
        clear()
        stripWhiteSpace(fn, f"{rootfolder}{stripfolder}" + f"{localfn.split('.', 1)[0]}-strip.{localfn.split('.', 1)[1]}")
    elif xt == "b" or xt == "B":
        clear()
        options()

# the read function takes fn and prints it out into the terminal
def read():
    
    print(f"Current File: {os.path.basename(fn)}")
    readActions()
    
    lc = 0

    for line in fileHandle:
        line = line.rstrip()
        lc += 1
        print(str(line) + "    AT: LINE " + str(lc))

    xt = input("\n\n[RN] to read a new file \n[B] to go back \n:")
    if xt == "RN" or xt == "rn" or xt == "Rn" or xt == "rN": 
        clear()
        inputFile()
        read()
    elif xt == "b" or xt == "B":
        clear()
        options()

# the beforeSearch function determines if the file you want to search is an index or regular file
def beforeSearch():
    print(f"Current File: {os.path.basename(fn)}")

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

# the searchIndex function searches the index file you input (fn)
def searchIndex():
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

# the search function is the classic LogSearcher. it takes an input file, searches it for a term, and can export the search terms and the lines in which they were found
def search():

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

#---------------------------------------------------
# Start the program
#---------------------------------------------------

fn = "empty"
options()