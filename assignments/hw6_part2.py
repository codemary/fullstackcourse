'''
Homework Assignment 6
part2
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
