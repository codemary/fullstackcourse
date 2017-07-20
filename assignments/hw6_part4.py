'''
Homework Assignment 6
part 4
'''

import math


def quadratic_equation(a, b, c):
    x = (b * b) - (4 * a * c)
    x = int(x)
    if x > 0:
        x = math.sqrt((b * b) - (4 * a * c))
        y1 = float(((-b) + x) / (2 * a))
        y2 = float(((-b) - x) / (2 * a))
        print("roots are real but not equal : y1:", y1, "  y2:", y2)
    elif x < 0:
        print("error: roots are complex :", x)
    elif x == 0:
        y1 = float((-b) / (2 * a))
        y2 = float((-b) / (2 * a))
        print("roots are real and double : y1:", y1, "  y2:", y2)


quadratic_equation(3, -6, 3)
