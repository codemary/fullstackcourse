from datetime import datetime, timedelta


'''
Homework Assignment 2
Part 2:
Question 4:
'''


def find_n_times_day(bday1, bday2, n):
    """bday1 is the older person.
    both birthdays are entered as tuples in this format:
    (year, month, day)"""

    bday1 = datetime.strptime(bday1, '%d/%m/%Y')
    bday2 = datetime.strptime(bday2, '%d/%m/%Y')
    person1 = datetime.date(bday1)
    person2 = datetime.date(bday2)

    age_diff = -(person1 - person2)

    p1 = int(age_diff.days)
    p2 = 0

    while p2 * n != p1:
        if p2 * n > p1:
            print("This never precisely occurred")
            return None
        p1 += 1
        p2 += 1

    date_at_n_times_age = person2 + timedelta(days=p2)

    print(date_at_n_times_age,
          "person 1 was %d days old, and person 2 was %d days old." % (p1, p2))


find_n_times_day("1/1/1880", "1/2/2001", 4)
