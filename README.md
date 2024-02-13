# LogSearcher
 a fast python program for searching large log files for errors and doing... other things

# How to use
the launcher will give you two options: local and remote.

## REMOTE
1. when the program asks for a URL for a file to test, paste in the URL of the log file you want to test. if it is an invalid file, the program will quit
2. input the search term, eg. the error you want to find
3. the program will ask to create a file containing the search hits. if you want to do so, refer to step 3-a
 3-a. the program will ask for a file name, include the file extention (such as .log)
 3-b. the program will ask for a folder in which to save the file. if the folder specified is not available, the program will create one
4. the program will find all the instances of that error message in the log file. if there are no instances of the term, you will be prompted to exit
5. after the program is finished with finding the instances, it will prompt to exit

## LOCAL
1. the program will start with a menu. start by adding a file [A], and put in the file location on your hard drive
2. after adding the file, you have a few options on actions you can do. if you have not added a file, the program will prompt you to do so.
 
 [S]: searches a file. it asks for a regular file or an index file. if the file you are inputting is not a .json created by the program, use R.
  1. Enter a search term.
  2. Choose if you want to create a file or not.
  3. The program will search the log file, print out the lines on which the search term was found, and create a file in the location specified with the name specified.

 **CURRENTLY BROKEN** If you searched an index file (has to be cleaned, will explain in [R]):
  1. Enter a search term.
  2. The program will find the search term in the index file and print it out.

 [R]: reads a file. it asks to index or strip white space in a file.
 
 [I]: indexes the input file. asks for a regular file or a file you want to clean. if you created an index before, you NEED to clean it so that you remove duplicate keys. exports files as *{filename}-index.{file extention}* or *{filename}-index-clean.{file extention}* in *root/index*
 
 [S]: strips white space in the target file and exports it as *{filename}-strip.{file extention}* in *root/strip*
 
 [C]: changes the root folder for indexes and strips. further explanation on usage in the program
 
 [E]: edit the file in an external editor, options are: **[V]: Vim**, **[NV]: Neovim**, **[N]: Notepad**, **[C]: VS Code**
 
 [B]: goes back to launcher
 
 [Q]: quits the program

# Contact
if you have issues with this program, you can contact me on Discord, my tag is alpenstorm there and also on [Reddit](https://www.reddit.com/user/alpenstorm) and [Twitter](https://twitter.com/alpenstorm)

# Help
if you run out of space, use a program such as [Tabby](https://tabby.sh/) to read large files (if you're not using file exporting, which is recommended), as the default Windows terminal runs out of space pretty quickly!

**GUI VERSION IS DISCONTINUED!!!**
