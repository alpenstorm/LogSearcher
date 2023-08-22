# This program is made for searching large log files for errors.

#---------------------------------------------------
# HOW TO USE
#---------------------------------------------------
# 1. when the program asks for a file location, paste in the location of the log file you want to test. if it is an invalid file, the program will quit
# 2. input the search term, eg. the error you want to find
# 3. the program will find all the instances of that error message in the log file. if there are no instances of the term, you will be prompted to exit
# 4. after the program is finished with finding the instances, it will prompt to exit

# made by alpenstorm


fn = input("Enter File Location: ")
try:
    fileHandle = open(fn)
except:
    print("File Cannot be opened", fn)
    quit()

trm = input("Enter Search Term: ")

tc = 0
lc = 0


for line in fileHandle:
    line = line.rstrip()
    lc = lc + 1
    if not str(trm) in line: 
        continue
    tc = tc + 1
    print(line)


print("Total Lines:", lc)
print("Terms Found:", tc)

xit = input("Press [Enter] to exit")
