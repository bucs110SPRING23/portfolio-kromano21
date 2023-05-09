import random
number = random.randrange(1, 1001)
guesses = []
x = 0
guess = int(input("Guess a number from one to one thousand: "))
while number != guess:
    if number > guess:
        print("Too low!")
    elif guess > number:
        print("Too High!")
    guesses.append(guess)
    guess = int(input("Guess a number from one to one thousand: "))
if guess == number:
    print("Correct!")
    guesses.append(guess)
for i in guesses:
    x += 1
print(number)
print(x, "guesses")
