import random
n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number:"))
    if guess > 0:
        if guess> to_be_guessed:
            print("Number to large")
        elif guess< to_be_guessed:
            print("Number is to small")
    else:
        print("Sorry that you're given up!")
        break
else:
    print("Congratulations you are grate")