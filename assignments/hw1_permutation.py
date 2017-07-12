def is_permutation(L):

    for v in range(1, len(L) + 1):
        if v not in L:
            return False

    return True


print(is_permutation([1, 1, 2, 3, 4, 5]))
