'''
Homework Assignment 2
Part 2:
Question-1,2 :
'''

from datetime import time, date, datetime


def age_calculator(birthday):

    birthday = datetime.strptime(birthday, '%d/%m/%Y %H:%M:%S')
    today = date.today()
    age = today.year - birthday.year
    if today.month <= birthday.month and today.day < birthday.day:
        age -= 1

    try:
        next_birthday = birthday.replace(year=today.year)
    except ValueError:
        # not a leapyear this year, no february 29th; use the day before
        next_birthday = birthday.replace(day=28, year=today.year)

    if next_birthday.date() < today:  # already passed this year, pick next year
        try:
            next_birthday = birthday.replace(year=today.year + 1)
        except ValueError:
            # not a leapyear next year, no february 29th, use the day before
            next_birthday = birthday.replace(day=28, year=today.year + 1)

    td = next_birthday.date() - today
    hours = next_birthday.time().hour - today.timetuple().tm_hour
    minutes = next_birthday.time().minute - today.timetuple().tm_min
    seconds = next_birthday.time().second - today.timetuple().tm_sec

    print("Hi your age is %d . Your next birthday is in %d days %d hours %d minutes %d seconds." %
          (age, td.days, hours, minutes, seconds))


age_calculator("25/06/1986 15:08:03")
