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

<<<<<<< HEAD
if the launcher prints out "Local searcher not found, please consult readme!", you have come to the right place. there are a couple of reasons why this error message might come up. first, check if the files in the py/ folder are named "logsearcher-local.py" and "logsearcher-remote.py". if they are named differently, you will get this error. please do not rename these files. if the error comes up again, try redownloading the program from [GitHub](https://github.com/alpenstorm/LogSearcher/releases). if the isssue persists, contact me and I will try to have it sorted out.
=======
if the launcher prints out "Local searcher not found, please consult readme!", you have come to the right place. there are a couple of reasons why this error message might come up. first, check if the files in the py/ folder are named "logsearcher-local.py" and "logsearcher-remote.py". if they are named differently, you will get this error. please do not rename these files. if the error comes up again, try redownloading the program from [GitHub](https://github.com/alpenstorm/LogSearcher/releases). if the isssue persists, contact me and I will try to have it sorted out.

if you get a traceback like this:

  File "C:\---\---\---\---\---\LogSearcher\launcher.py", line 8, in <module>
    exec(fl.read())
  File "<string>", line 85, in <module>
  File "C:\---\---\AppData\Local\Programs\Python\Python311\Lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  UnicodeDecodeError: 'charmap' codec can't decode byte 0x8f in position 3846: character maps to <undefined>

or

Traceback (most recent call last):
  File "C:\---\---\---\---\---\LogSearcher\py\logsearcher-local.py", line 85, in <module>
    for line in fileHandle:
  File "C:\---\---\AppData\Local\Programs\Python\Python311\Lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 UnicodeDecodeError: 'charmap' codec can't decode byte 0x8f in position 3846: character maps to <undefined>

this means that the document you're trying to read has a character that Python can't decode. im working on a fix for this, and i'll update the readme when it is done
