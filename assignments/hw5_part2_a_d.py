'''
Homework Assignment 5
Part 2
answers(a)(d)
'''


def count_all_enrolled_students(d):
    all_students = []
    for k, v in d.items():
        all_students.extend(v)
    return len(list(set(all_students)))


def hold_workshop(d):
    list_of_students = []
    python101_students = []

    for k, v in d.items():
        if k == "python101":
            python101_students.extend(v)
            continue
        list_of_students.extend(v)

    for student in list_of_students:
        if student in python101_students:
            list_of_students.remove(student)

    return list(set(list_of_students))


registrations = {
    "python101": ["ram", "shyam", "mohan"],
    "c": ["mohan", "rohan", "shaktiman"],
}

print(count_all_enrolled_students(registrations))

print(hold_workshop(registrations))
