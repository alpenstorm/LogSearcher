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

fn = input("Enter File Location: ")

try:
    fileHandle = open(fn, "r", encoding="utf8", errors="ignore") 
except:
    print("File cannot be opened", fn)
    quit()

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
        
            print("\nFound", tc, "terms \n In", lc, "lines \n From location", fn, "\n")

            xt = input("Press [Enter] to exit")
        
            if xt == "\n": quit()
            else: quit()
    
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
        
            print("\nFound", tc, "terms \n In", lc, "lines \n From location", fn, "\n")

            xt = input("Press [Enter] to exit")
        
            if xt == "\n": quit()
            else: quit()

for line in fileHandle:
    line = line.rstrip()
    lc += 1
    if not str(trm) in line: 
        continue
    tc += 1
    print(str(line) + "    AT: LINE " + str(lc))


print("\nFound", tc, "terms \n In", lc, "lines \n From location", fn, "\n")

input("Press [Enter] to exit")