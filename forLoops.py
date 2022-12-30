number = " 999,345:678;444 789:234;456"
separators = ""  # range is an iterator
for char in number:
    if not char.isnumeric():
        separators = separators + char
print(separators)

print("-" * 30)

string = "Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order," \
         "Irrigation, Roads, the Fresh-Water System, and Public Health, what have the " \
         " Romans ever done for us?"
capitals = ""
for char in string:
    if char.isupper():
        capitals = capitals + " " + char
print(capitals)
print("-" * 30)
for i in range(0, 11,2):  # range iterator gives range of number
    # from the starting value upto but including end value
    # no start value defaults to 0, if step value added then start value must
    print(i)
print("-" * 30)
for i in range(10,0,-2): # backwards swap start and end value
    print(i)
print("-" * 30)
for i in range(0,100):
    if i%7==0:
        print(i)
