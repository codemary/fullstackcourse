'''
Homework Assignment 6
part 2, 3
'''


def countdown(string):
    try:
        isNumber = int(string)
        return True
    except ValueError:
        print("Not an integer!")
        return False


user_input = input("Input: ")
isNumber = False

while not isNumber:
    if(countdown(user_input)):
        isNumber = True
        i_input = int(user_input)
    else:
        user_input = input("Please enter an integer: ")

while(i_input < 0):
    user_input = input("Enter a positive number: ")
    # Need to check if input is a number again
    isNumber = False
    while not isNumber:
        if(countdown(user_input)):
            isNumber = True
            i_input = int(user_input)
        else:
            user_input = input("Please enter an integer: ")
    i_input = int(user_input)
while(i_input >= 0):
    print(i_input)
    i_input -= 1


base = input("Raise... ")
exp = input("to the power of... ")
isNumber = countdown(base) and countdown(exp)
while not isNumber:
    base = input("Please enter a base that's a number. ")
    exp = input("Please enter an exponent that's a number. ")
    isNumber = countdown(base) and countdown(exp)
i_base = int(base)
i_exp = int(exp)
answer = 1
for i in range(i_exp):
    answer *= i_base
if i_base == 0:
    answer = 0
if i_exp == 0:
    answer = 1
print(base + " raised to the power of " + exp + " is " + str(answer))
