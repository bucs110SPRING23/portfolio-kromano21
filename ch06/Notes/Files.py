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

