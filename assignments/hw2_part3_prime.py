'''
Homework Assignment 2
Part 3
'''


def is_prime(n):
    if n < 1000000:
        for i in range(3, n):
            if n % i == 0:
                return False
        return True

    else:
        return False


print(is_prime(14734354354))
