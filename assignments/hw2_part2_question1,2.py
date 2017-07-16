'''
Homework Assignment 2:
Part 2: 
Answer 2:
'''

from datetime import time, date, datetime, timedelta


def find_double_day(bday1, bday2):
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

    while p2 * 2 != p1:
        p1 += 1
        p2 += 1

    date_at_twice_age = person2 + timedelta(days=p2)
    print("Date at twice age: ", date_at_twice_age,
          ", Person 1 was %d days old, and person 2 was %d days old" % (p1, p2))


find_double_day("29/12/1990", "30/5/2001")
