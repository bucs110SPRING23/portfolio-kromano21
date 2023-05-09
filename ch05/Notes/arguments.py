#Data Arguments
#Functions are stored algorithms. Algorithms act on data.
#Without data, an algorithm is just a set of instructions.
#When we give data to a function, the data is called an argument. 
#Always get data outside of a function and then pass those values in as arguments.

#Parameters
#Parameters define the type of data a function needs
#Ex: The input() function takes a str, any str, as a parameter
#A function must declare what parameters it can take

import turtle
def foo():
    print("nothing")

def bar(x, y):
    print(x, y)

foo(5) #prints error because foo declares no parameters
bar('5', '7', '9') #error because only 2 parameters declared

#Parameters Define
#1. The order you are going to take the arguments in your function 
#2. What name you are going to use for the argument inside the function

#Define parameters inside the paranthesis using the same naming conventions as variables

#Named Parameters 
#We can assign a default value to a parameter to make it optional 
def funct_with_default_params(arg1=0, arg2=""):
    print(arg1, arg2)

funct_with_default_params(arg=1) #arg2 will be set to the default 

#providing a default value, also called a named parameter, also lets you pass arguments in any order
#For Positional Parameters arguments are required and must be passed in the correct order
#For named paramters arguments are optional and can be passed in any order
#You can use both positional and named parameters, but named parameters must come after positional parameters
#A local variable is any variable defined inside a function
#Parameters are local variables 
#Any local variables are deleted at the end of the function
#Local variables can only be accesed within a function
#Where you can use a variable is known as a variable's scope