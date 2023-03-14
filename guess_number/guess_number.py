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

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Yay! The computer guessed your number, {guess}, correctly")

computer_guess(10)

