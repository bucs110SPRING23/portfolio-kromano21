import random
#Part A
weeks = 16
print(weeks, type(weeks))
classes = 5
print(classes, type(classes))
tuition = 6000
print(tuition, type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print(cost_per_week, type(cost_per_week))
print("Cost per week:", cost_per_week)
classes_per_week = 15
print(classes_per_week, type(classes_per_week))
cost_per_class = (cost_per_week / classes_per_week)
print(cost_per_class, type(cost_per_class))
print("your cost per class is", cost_per_class, "dollars")
#Part B
mylist = [1, 2, 3, 4, 5]
mylistoutput = random.choice(mylist)
print(mylistoutput)
