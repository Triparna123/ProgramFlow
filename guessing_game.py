answer=5
print("Please enter a number between 1 and 10")
guess=int(input())
if guess<answer:
    print("Guess higher")
elif guess > answer:
    print("guess lower")
else:
    print("guessed correct")
