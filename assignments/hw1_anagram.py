def anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    if len(s1) != len(s2):
        print("incorrect length")
        return False

    skip = []

    for l in s1:
        if l in skip:
            continue
        if s1.count(l) != s2.count(l):  # costly op
            return False

        skip.append(l)

    return True


print(anagram("I am Lord Voldemort", "Tom Marvolo Riddle"))
