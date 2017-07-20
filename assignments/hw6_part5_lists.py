'''
Homework assignment 6
Part 5
'''
# answer 1:
print[x**3 for x in range(1, 11)]

# answer 2:


def vowels(chars):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [x for x in chars if x in vowels]


print vowels("vowels")

# answer 3:

[x + y for x in [10, 20, 30] for y in [1, 2, 3]]

for x in [10, 20, 30]:
    for y in [1, 2, 3]:
        y = x + y
        print(y)
