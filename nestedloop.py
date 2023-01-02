for i in range(1, 5):
    for j in range(1, 7):
        print("{} times {} is {}".format(j, i, i * j))
    print("--------")

for i in range(0, 5):
    for j in range(0, 3):
        print(end=" ")
    for j in range(0, 6):
        print("*", end=" ")
    print()

print('---' * 30)

shopping_list = ["milk", "bread", "spam", "eggs"]
for item in shopping_list:
    if item != "spam":
        print(item)
print('---' * 30)

for item in shopping_list:
    if item == "spam":
        continue  # continue ignores all other lines of code in the loop if that item is found
        # when spam found it goes back to line 21 for next item instead line 24
    print(item)
print('---' * 30)

item_to_be_found = "albastross"
found_at = None  # None is a constant means nothing. When this line executes
# the variable exists but does not have a value
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_be_found:
        found_at = index
        break  # terminates the loop after found the item in the list
if found_at is not None:
    print(found_at)
else:
    print(" Item not found")
print('---' * 30)

# if item is not present in the list it will return value None because of line 29 , i
# f we hadn't initialized found_at then if the item was not present in the list then it would
# provide an error but if the item present then it will return value of index of the item found
