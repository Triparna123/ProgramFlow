# for i in range(10):  for loop iterates for a pre-defined sequence
#     print(i)

i = 0
while i < 10:  # while loop is useful in cases where we don't know for how many times we need to loop
    # ex: reading data from a file
    print(i)
    i += 1

available_exists = ["north", "south", "east", "west"]
chosen_exists = ""
while chosen_exists not in available_exists:
    chosen_exists = input("Please enter a direction ")
    if chosen_exists.casefold()=="quit":
        print("Game over")
        break
print("you are out ")



