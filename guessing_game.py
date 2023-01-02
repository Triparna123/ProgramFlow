import random  # random is a python built module generator

lowest = 1
highest = 10
answer = random.randint(lowest, highest)  # randint is a function present in the random module the module
# is differentiated from the module function with a dot notation
# randint is a function that returns a random number from the range we specified
print(answer)
guess = 0
print("Please enter a number between {} and {}".format(lowest, highest))
while guess != answer:
    guess = int(input())
    if guess == 0:  # to exit the program if cannot guess correctly for a long time
        break
    if guess == answer:
        print("guessed correct")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # if guess is greater than answer
            print("Please guess lower")

# guess = int(input)
# if guess == answer:
#     print("guessed correct")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:  # if guess is greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done")
#     else:
#         print("Sorry you have not guessed it correctly")

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else: # if guess is greater than answer
#         print("Please guess lower")
#     guess=int(input())
#     if guess == answer:
#         print("Well done")
#     else:
#         print("Sorry you have not guessed it correctly")
# else:
#     print("guessed correct")


# if guess<answer:
#     print("Guess higher")
#     guess=int(input())
#     if guess == answer:
#         print("Well done ")
#     else:
#         print("Sorry you have not guessed it correctly")
# elif guess > answer:
#     print("guess lower")
#     if guess == answer:
#         print("Well done ")
#     else:
#         print("Sorry you have not guessed it correctly")
# else:
#     print("guessed correct")
