answer = 5
print("Please enter a number between 1 and 10")
guess = int(input())

if guess == answer:
    print("guessed correct")
else:
    if guess < answer:
        print("Please guess higher")
    else:  # if guess is greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done")
    else:
        print("Sorry you have not guessed it correctly")

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
