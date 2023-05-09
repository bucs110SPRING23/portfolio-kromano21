#Files are for storing program data 
#Every file is just the saved state of some program 
#Permament data is data that must be maintained when a program isn't running 
#Files are managed solely by the Operating System, which means you have to ask the OS to open the file for you

#Opening a File 
#When opening a file you must tell the OS
#1. Where is the file 
#2. name of the file
#3. How you are going to use the file

open(filename)

#Read Operations 
read()
#Reads the entire file into a single string 
#Returns a string 
readline()
#Reads the next line from the file 
#Returns a string
readlines()
#Reads all lines in the file into a list
#Returns a list of string objects
for
#loops by line through the file 
for line in myFile:
    print(line)
#Pointer
#Every file has an internal pointer
#The pointer is set to the beginning of the file when you open it. 
#Each operation advances the file's pointer automatically 

#Write Operations 
#You can use a file stream to either read or write, not both
#File Streams are one-way
#We can open a file stream, not both 
#To write a file, we need to open it specifically for writing 
#If the file does not exist, it will be created
#If the file does exist, all its content will be deleted in write mode
file_pointer = open("myideas.txt", 'w')// #using the 'w' flag
#Write a file by passing a string to the write() method
file_pointer.write('Time Stopper\n')
#Write does not work like print. You need to add the newline(\n)

#Append mode
file_pointer = open("myideas.txt", "a")
file_pointer.write("Time Starter")

#Closing a File
#You should close a file when you are done with it because
#1. You cannot open a new file stream to this file while the previous stream is open 
#2. Writing to a file doesn't happen immediately
#When your program ends, all program data is deleted, including data not yet written 
#If your code crashes before all the data is written, the data is lost 
#Closing the file forces Python to write the rest of the file 

#To close a file:
file_pointer.close()

