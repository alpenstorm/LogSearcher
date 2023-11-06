---------------------------------------------------
# LogSearcher
---------------------------------------------------
 a fast python program for searching large log files for errors

---------------------------------------------------
# How to use
---------------------------------------------------
1. when the program asks for a file location, paste in the location of the log file you want to test. if it is an invalid file, the program will quit

2. input the search term, eg. the error you want to find

3. the program will ask to create a file containing the search hits. if you want to do so, refer to step 3-a

    3-a. the program will ask for a file name. files are automatically created in .lsoutput, so name the file without an extention. if you want to disable this, check the comment on line 38 of either program

    3-b. the program will ask for a folder in which to save the file. if the folder specified is not available, the program will create one

4. the program will find all the instances of that error message in the log file. if there are no instances of the term, you will be prompted to exit

5. after the program is finished with finding the instances, it will prompt to exit

---------------------------------------------------
# Contact
---------------------------------------------------
if you have issues with this program, you can contact me on Discord, my tag is alpenstorm there and also on [Reddit](https://www.reddit.com/user/alpenstorm) and [Twitter](https://twitter.com/alpenstorm)

---------------------------------------------------
# Help
---------------------------------------------------
if you run out of space, use a program such as [Tabby](https://tabby.sh/) to read large files (if you're not using file exporting, which is recommended), as the default Windows terminal runs out of space pretty quickly!