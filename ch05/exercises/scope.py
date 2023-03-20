def multiply(x, y):
    accumulator = 0
    for _ in range(y):
        accumulator = accumulator + x 
    return accumulator

def exponent(x, y):
    accumulator = 1
    for _ in range(y):
        accumulator = accumulator * x 
    return accumulator

def square(x):
    return multiply(x, x)

x=int(input("What is x?"))
y=int(input("What is y?"))
result = multiply(x, y)
print(result)
result = exponent(x, y)
print(result)
result = square(x)
print(result)
