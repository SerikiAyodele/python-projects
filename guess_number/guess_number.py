import random

def guess(x):
    random_number = random.randint(1,x)
    guessed =0
    while guessed != random_number:
        guessed = int(input(f"guess the number between 1 and {x}:"))
        if guessed > random_number:
            print("your guess was too high :)")
        elif guessed < random_number:
            print("your guess was too low :)")
    print("that's correct!")


guess(20)