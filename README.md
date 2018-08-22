# pythonic-fast-text-search
  A fast way to check in txt files by chunking the opening and managing the pattern match at byte level.

* Collect the patterns, in a txt file, which you want to check and/or find your big list of huge txt data files
* Set-up the variables in read_chunk
  - path_to_list -> It is the list of patterns you want to check (ex. r"C:\\python_projects\\read-text\\list_to_check.txt")
  - path_to_file_to_check -> It is the path to the folder wher you have one or more data files to check (ex. r"C:\\python_projects\\read-text\\data\\")
  - path_to_log_file -> It is your path to log file which will be create or overwritten once the script complete (ex. r"C:\\python_projects\\read-text\\filelog.txt")
3 Launch the read_chunk.py from console
 
**Note:**
In ../test there is the simple methods with lambda-function to check the pattern, created for test case.

**Source:**
Thanks to: http://stupidpythonideas.blogspot.com/2014/07/three-ways-to-read-files.html

 

