#A Pythonic way to search patterns in huge text files. Written by DSalvigni.

#Imported libraries
import csv
import os

#Set up my path:
#File with the list of PO to check
path_to_list = r"C:\\python_projects\\read-text\\list_to_check.txt"
#File the PO data to check
path_to_file_to_check =  r"C:\\python_projects\\read-text\\data\\"
#Path to my final generated log file with the results
path_to_log_file = r"C:\\python_projects\\read-text\\filelog.txt"

#Create the list of pattern to check
with open(path_to_list, 'r') as f:
  reader = csv.reader(f)
  list_of_patterns = list(reader)

#Function to clean text from list of chars  
def clean_text(text, dic):
 for i, j in dic.items():
  text = text.replace(i, j)
 return text

#I create the list of char to replace  
dict = { "[": "", "]":"", "'":""}

#I initialize an empty list to push in the results
results = []
i = 0
  
#We iterate for each patter a research  
for pattern in list_of_patterns:
 #I clean the pattern from strange chars
 pattern=clean_text(str(pattern),dict)
 #I format the pattern to match what I am trying to catch. In this case the format text02 = 'nnnnnnnnn | |xx' withouth 0-leading
 #Here is possible to use also a REGEX.
 pattern=((pattern[:11]).lstrip('0')).replace("|"," | |")+((pattern[11:17]).lstrip('0'))
 print('START Analysis to find the following pattern -> '+pattern+': ')
 #for each file in the given path_to_file_to_check directory, the pattern will be checked to be find, in byte reading mode
 for directory, subdirectories, files in os.walk(path_to_file_to_check):
  for file in files:
   path_to_file = str(os.path.join(directory, file))
   with open(path_to_file, 'rb') as f:
    #The chunck dimension can be changed as preferred
    for chunk in iter(lambda: f.read(4096), b''):
     if str.encode(pattern) in chunk:
      i= i + 1
      print('Found '+pattern+' - Number of Occurencies -> '+str(i))
      here_there_is_a_match = pattern+': found in -> '+path_to_file_to_check+"\n"
	  #If I find somthing I append the result in a list
      results.append(here_there_is_a_match)
	  
#FInally I save the results in a log file
logfile = open(path_to_log_file,'w')	   
for result in results:
  logfile.write(result)
logfile.close()
