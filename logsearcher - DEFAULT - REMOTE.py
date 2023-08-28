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
#fn = input("Enter File Location: ") # if this is commented, uncomment it to read local files
fn = input("Enter URL: ")
#---------------------------------------------------

try:
    #fileHandle = open(fn)
    fileHandle = urllib.request.urlopen(fn)
except:
    print("File cannot be opened", fn)
    quit()

trm = input("Enter Search Term: ")

tc = 0
lc = 0

for line in fileHandle:
    #line = line.rstrip() # if this is commented, uncomment it to read local files
    line = line.decode().strip() # if this is commented, uncomment it to read remote files
    lc = lc + 1
    if not str(trm) in line: 
        continue
    tc = tc + 1
    print(line)


print("Total Lines:", lc)
print("Terms Found:", tc)

input("Press [Enter] to exit")