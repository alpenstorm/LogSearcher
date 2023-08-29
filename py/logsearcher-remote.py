# This program is made for searching large log files for errors.
# if you want to make the program search a file hosted on the internet, uncomment all the lines in the code

#---------------------------------------------------
# HOW TO USE
#---------------------------------------------------
# 1. when the program asks for a file location, paste in the location of the log file you want to test. if it is an invalid file, the program will quit
# 2. input the search term, eg. the error you want to find
# 3. the program will find all the instances of that error message in the log file. if there are no instances of the term, you will be prompted to exit
# 4. after the program is finished with finding the instances, it will prompt to exit

# made by alpenstorm


# [uncomment/comment] these if you want to [use/not] web searching
#---------------------------------------------------
import urllib.request
import urllib.parse
import urllib.error
#---------------------------------------------------


# [uncomment/comment] these if you want to [use/not] web searching
#---------------------------------------------------
#fn = input("Enter File Location: ")
fn = input("Enter URL: ")
#---------------------------------------------------

try:
    #fileHandle = open(fn) # if this is commented, uncomment it to read local files
    fileHandle = urllib.request.urlopen(fn) # if this is commented, uncomment it to read remote files
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
    with open(foldern + filen + ".lsout", "w") as output:
        output.write("------OUTPUT FILE CREATED------"+ "\n\n")

        for line in fileHandle:
            #line = line.rstrip()
            line = line.decode().strip() # if this is commented, uncomment it to read remote files
            lc += 1
            if not trm in line:
                continue
            tc += 1
            output.write(line + "\n\n")
            print(line + "AT: LINE" + str(lc))
        
        output.write("------OUTPUT FILE FINISHED------")
        
        print("Total Lines:", lc)
        print("Terms Found:", tc)

        xt = input("Press [Enter] to exit")
        
        if xt == "\n": quit()
        else: quit()



for line in fileHandle:
    #line = line.rstrip() # if this is commented, uncomment it to read local files
    line = line.decode().strip() # if this is commented, uncomment it to read remote files
    lc += 1
    if not str(trm) in line: 
        continue
    tc += 1
    print(str(line) + "AT: LINE" + str(lc))


print("Total Lines:", lc)
print("Terms Found:", tc)

input("Press [Enter] to exit")
