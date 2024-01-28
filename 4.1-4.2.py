import random
# author, Caige laurenti
#guessing game program
secret = random.randint(1, 10)

while True:
    print("enter a integer 1-10")
    guess = int(input("Enter your guess: "))

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Just right!")
        break