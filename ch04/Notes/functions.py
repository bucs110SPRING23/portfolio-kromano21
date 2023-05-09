#Vending Machine 
#Black boxing - Once we determine that a function works, we don't care how it works 

print("Welcome to the vending machine")
code = input("Please enter a code: ")
money = input("Give me money: ")

def my_vending_machine():
    if code == "A":

def find_max():
    print("Please enter 3 numbers:")
    a = int(input(": "))
    b = int(input(": "))
    c = int(input(": "))

    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    
    print(max)

#Single Responsibility Principle 
#A function should do one thing
#This function breaks the principle because it both takes and analyzes a set of inputs
#Collision - two variables of the same name 
#can't have variables of the same name in the same scope 

def foo(var): #Function Scope: var = var{5}
    var += 1 #using the same name as a global variable is called shadowing 
    print(var)

var = 5
foo(var)
print(var)