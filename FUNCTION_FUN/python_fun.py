import random

comp_num = random.randint(1, 100)

while True:
    try:
        user_num = int(input("Guess the number: "))
        if user_num > comp_num:
            print("too big!")
        elif user_num < comp_num:
            print("too small")
        else:
            print("You win")
            break
    except ValueError:
        print("Its not a number!")

