#Files
#Saved Program State
#Operating System - manage files
#request file from operating system 
# - where
# - name
# - how to use it 

#working with files is one way 
def main():
    file_pointer = open("ideas.txt")
    ideas = file_pointer.read()
    print(ideas)
    ideas = file_pointer.readlines()
    print(ideas)
    ideas = file_pointer.readline()
    file_pointer.close()
    idea = input("Enter an idea")
    ideas = []
    ideas.append(idea)
    print(ideas)
main()

file_pointer = open("assets/ideas.txt", "a") #the file gets truncated #"a" - append mode, automatically moves to end 

idea = input("Enter an idea: ")
ideas = []
ideas.append 
for i in ideas:
    file_pointer.write(i + "/n") #/n is the symbol for a line break, /t for tab, 

main()


""" file_contents = open("assets/ideas.txt", "r") #modes: 'r', 'w', 'a'
file_contents = file_pointer.read() #entire file in a single string """
file_contents = file_pointer.readline() #first line as a string 
file_contents = file_pointer.readline() #second line as a string
for line in file_pointer:
    print(line)

#Gets lines as in a list

#File Streams - one way 
file_contents = open("assets/ideas.txt", "r") #modes: 'r', 'w', 'a'
#'w' - deletes any existing file (truncates)
file_pointer.write("Hello World") #Does not add the newline <enter> like print 
file_pointer.write("/n") #space, backlash
file_pointer.close() #always close files when writing

#'a' = appends to the file 
file_pointer = open("assets/ideas.txt", 'a')
var = 5/0
