#While Loop
#For Loops can solve two problems
#1. They can loop to operate on all items in a list
#2. They can loop sequentially a specific number of times

#How could the following algorithm cause a problem with a for loop?
#1. Take input from a user
#2. Check the input to see if it is correct
#3. If it is correct, continue on
#4. Otherwise ask the user again for input

#We do not know how many times we are going to need to loop
#We need a loop that acts like an if statement. In other words, a loop that repeates itself until the boolean expression elvaluates to false
#The While Loop is a for loop and an if statement combined
#If the condition elvaluates to True exectute the block 
#Loop and check boolean expression again 
#If the boolean expression elvaluates to True execute the block 
#Stop looping once the boolean expression elvaluates to false 
""" iterating_var
while <boolean expression>:
    <operations> #must alter iterating variable

for i in range(0, 10):
    print(i)

i = 0
while i < 10:
    print(i)
    i = i + 1 """

#Any for loop can be created with a while loop but not all while loops can be recreated with a for loop

#An Adding Program
#print("Please enter a series of numbers to sum ['q' to quit]: ")

""" sum = 0
while sum != 'q':
    value_to_add = input(':')
    if value_to_add.isdigit():
        value_to_add = int(value_to_add)
        sum += value_to_add # equivalent to: sum = sum + value_to_add
    elif value_to_add == 'q':
        print("your current sum is sum is: ", sum)
        sum = value_to_add
print("all done") """

#Infinite Loops
#What happens if the boolean expression values never change
import random
i = 0
while i < 5:
    print(i)
    if random.randrange(5) == 3:
        i += 1
