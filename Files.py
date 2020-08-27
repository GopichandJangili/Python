#remove duplicates in numpy
import numpy as np

a = np.array([1,2,3,4,1])
a = np.unique(a)
print(a)
#eval function
print('1+2')
print(eval('1+2'))
x,y=10,20
print(eval('x+y'))


######################################################
#####################File Handling####################
######################################################
#Key Points
'''
1. The open() function takes two parameters; filename, and mode.
2. There are four different methods (modes) for opening a file:
    "r" - Read - Default value. Opens a file for reading, 
          error if the file does not exist
    "a" - Append - Opens a file for appending, creates the file if it does not exist
    "w" - Write - Opens a file for writing, creates the file if it does not exist
    "x" - Create - Creates the specified file, returns an error if the file exists
'''

import os
path = r'C:\Test\Test'
#create files
#method one
read_file = open(path+'//test.txt','w')
read_file.write('abcd')
read_file.close()

#method two
string = 'abcd'
with open(path+'//test_1.txt','w') as f:
    f.write(string)

#Difference between open and with open
'''
Basically, using with just ensures that you don't forget to close() the file,
making it safer/preventing memory issues
'''




#Notes
'''
we can only remove empty folders
'''


#List all files and dicrectories in a path


#to check for directory
x = os.path.isdir(path+'\\'+'New folder') #True
y = os.path.isdir(path+'\\'+'New fold') #False
print(x,y)
#to check for files
p = os.path.isfile(path+'\\'+'New Text Document.txt') #True
q = os.path.isfile(path+'\\'+'sample.txt') #False
print(p,q)

#lists all (both files and directories
#we can separate them by using list comprehension
s = os.listdir(path)
print(s)

folders = [x for x in s if os.path.isdir(path+'\\'+x)]
print(folders)

files = [x for x in s if os.path.isfile(path+'\\'+x)]
print(files)


