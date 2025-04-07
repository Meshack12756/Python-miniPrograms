import random
random_number = random.randint(1, 20)

while True:
    user_number = int(input("Guess a number between 1 and 20; "))
    if user_number.isapha():
        print("Error!! Please input an integer.")
    elif user_number == random_number:
        print("Correct! You guessed the correct number.")
        break
    elif user_number > random_number:
        print("Too High!!")
    else:
        print("Too low!")
