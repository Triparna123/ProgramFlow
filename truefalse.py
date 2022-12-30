# conditional operator: < > <= >= == !=
# boolean operator: and ,or ,not ,in, not in
# any object can be tested for truth value for use in if or while condition
# builtins considered to be false: None,False,0 of any numeric type,
# empty sequence(str) and collection
# 1 is considered as True

# if 0:
#     print("False")    #this line is unreachable since 0 evaluates to false
# else:
#     print("True")
name = input()  # if we put an empty string in input then else executed
if name:  # if name is true
    print("Hello")
else:
    print("No name")
