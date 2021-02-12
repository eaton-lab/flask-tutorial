#!/usr/bin/env python

"""
Functions for sipmle hello-world type code.
"""

import datetime

# YEAR THE ORIGIN OF SPECIES WAS PUBLISHED
DARWINDAY = datetime.datetime(1809, 2, 12)


def days_to_dday():
    """
    Returns number of days to next Darwin day
    """
    next_year = datetime.datetime.today().year + 1
    next_dday = datetime.datetime(next_year, 2, 12)
    diff = next_dday - datetime.datetime.today()
    return diff.days


def age_to_darwin(year, month, day):
    """
    Return the number of days by which you are older or younger than
    Charles Darwin.

    Paramters
    ---------
    year (int):
        Year the person was born.
    month (int):
        Month the person was born.
    day (int):
        day of month the person was born.
    """
    # return number of days from today to NEXT DDAY
    birthdate = datetime.datetime(year, month, day)
    diff = birthdate - DARWINDAY
    return diff.days


if __name__ == "__main__":
    print(f"It is {days_to_dday()} days until Darwin Day")
    print(f"Deren is {age_to_darwin(1985, 3, 30)} days younger than Darwin")
