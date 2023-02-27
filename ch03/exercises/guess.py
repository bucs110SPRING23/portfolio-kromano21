import random
number = random.randrange(1, 1000)
guess = int(input("Guess a number from one to ten: "))
if number == guess:
    print("Correct!")
elif number > guess:
    print("Too Low!")
    guess2 = int(input("Try Again: "))
    if guess2 == number:
        print("Correct!")
    elif guess2 > number:
        print("Too High!")
        guess3 = int(input("Try one more time: "))
        if guess3 == number:
            print("Correct!")
        elif guess3 > number:
            print("Too high. You Lose!")
        elif guess3 < number:
            print("Too low. You Lose!")
    elif guess2 < number:
        print("Too Low")
        guess3 = int(input("Try one more time: "))
        if guess3 == number:
            print("Correct!")
        elif guess3 > number:
            print("Too high. You Lose!")
        elif guess3 < number:
            print("Too low. You Lose!")
elif number < guess:
    print("Too High!")
    guess2 = int(input("Try Again: "))
    if guess2 == number:
        print("Correct!")
    elif number > guess2:
        print("Too Low!")
        guess3 = int(input("Try one more time: "))
        if guess3 == number:
            print("Correct")
        elif guess3 > number:
            print("Too High. You Lose!")
        elif guess3 < number:
            print("Too low. You Lose!")
    elif guess2 > number:
        print("Too high!")
        guess3 = int(input("Try one more time: "))
        if guess3 == number:
            print("Correct")
        elif guess3 > number:
            print("Too High. You Lose!")
        elif guess3 < number:
            print("Too low. You Lose!")






