# The if statement is a conditional statement that executes based on the result of the boolean expression
# If money >= cost
    #print("Here is your change:", money - cost)
#else
    #print("Not enough money")

#if BOOLEAN_EXPRESSION:
    #code...
#else:
    #other code...

#you can omit the else clause
#if Boolean_Expression:
    #code...

#if x: (elavluates to false, this program only prints: "Done")
    #print(x)
#print(done)

#-Statements end with a :
#The code block you want to run when the if elvaluates to True must be indented
#Only one block in an if statement is ever going to run 
#else does not have a condition 
#Any valid python function? can go in an if statement, including more if statements 

#elif
#elif allows you to add additional exlusive conditions to your if statement
#You can unlimited elif clauses between the if and the else, but only ONE will run 
#if statements are checked in order
#The first match and only the first match runs

#Write the code to (without elif)
#1. Check if a number is greater than 5
#2. Then check if a number is also greater than 10, print out "A lot"
#3. Otherwise print "some"
#4. else print out: "a few"
x = 5
y = 5
if x>= 5:
    if x>= 10:
        print("A lot")
    else:
        print("some")
else:
    print("a few")
#elif
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")

#Final Else
#A single and optional final else statement does not have a condition.^
#When more than one condition is true, only the first true branch executes. 
#Therefore, when using elif the most restrictive case should always go first. 



