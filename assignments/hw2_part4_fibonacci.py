'''
Homework Assignment 2
Part 4
'''


def fibonacci(n):
    n0 = 0
    n1 = 1
    if n == 1:
        print(n0)
        return
    if n == 2:
        print(n1)
        return

    print(n0)
    print(n1)

    for i in range(2, n):
        next = n0 + n1
        if next >= n:
            break
        print(next)

        n0 = n1
        n1 = next


fibonacci(7)
