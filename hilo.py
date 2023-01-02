# in guessing_game.py we let user input the guess number .
# Here we will let computer guess a number by implementing the binary search algorithm.
# Binary search algorithm works on a ordered set of data to search a item in more efficient and fast way.
# It divides the sequence into half each time guessed which reduces
# the search within 10 guesses at most for range 1 to 1023. 2 times 10 is 1023 since halved we take 2

low = 1
high = 1000
print("Enter a number between {} and {} ".format(low, high))
guesses = 1
while True:
    print("\t Guessing in the range of {} and {} ".format(low,high))
    guess = low + (high - low) // 2  # formula for binary search
    high_low = input("My guess is {} . Is my guess correct or should i guess higher or lower? "
                     "Enter h for higher,l for lower or c for correct ".
                     format(guess)).casefold()
    if high_low == "h":  # Guess higher, the low end will be one greater than the guess
        # pass  # pass keyword is used in Python to make the code syntactically correct.
        # We can type the rest of the code block later and not get an syntax error if given this keyword.
        low = guess + 1
    elif high_low == "l":  # guess lower, the high end will be one less than the guess
        # pass
        high = guess - 1
    elif high_low == "c":
        print("You have guessed it in {} guesses ".format(guesses))
        break
    else:
        print("Enter h,l or c")
    guesses = guesses + 1
