var1_data = 1
print(var1_data + 6)
print(var1_data + 6)
print(var1_data + 3467)

#"1" - string
#1 - integer

var1_data = "7"
print(type(var1_data))

print(7, "7")#types
#Variables like a bucket of data
- put things in 
- Take things out
- pass them around 
numbers, letters, underscores, no spaces, must start with a lowercase letter

'=': assingment operator, programmers refer to it as equal 
#3 data types of Python = int, flow, string
#container types
- data that only holds other data 
#list
mylist = [1, "2", 3, 4.0, [5, 6, 7, 8, 9, 10]]
#can insert different types inside the same list ^
#can create a list inside of a list^

print(mylist[0]) #0 indexed
print(mylist[2])
print(mylist[-1])
print(mylist[-2])
#print(mylist[8]) #ERROR

#can break a list across multiple lines 
mycolors = [
    "red",
    "green",
    "blue"
]

print(mycolors, len(mycolors))

mycolors[1] = "purple"
#changes green because first entry is 0 

#add yellow
mycolors.append("yellow")
print(mycolors)
#delete color
del mycolors[2]

var = 4
print(str(var)+ " is a number")
print(float(var) " is a number")

var = 4.0
float(var)
int(var) #error
