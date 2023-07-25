# Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

# 1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0).
# 2. If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine = 15 Hackos * (the number of days late).
# 3. If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine = 500 Hackos * (the number of months late).
# 4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.

# Charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018, that is a year late and the fine would be 10000 Hackos.

# Example
# d1, m1, y1 = 14, 7, 2018
# d2, m2, y2 = 5, 7, 2018

# The first values are the return date and the second are the due date. The years are the same and the months are the same. The book is 14 - 5 = 9 days late. Return 9 * 15 = 135.

# Return the fixed fine if the book is returned after the calendar year in which it was expected.

# Sample Input
# 9 6 2015
# 6 6 2015

# Sample Output
# 45

# Explanation
# Given the following dates:
# Returned: d1 = 9, m1 = 6, y1 = 2015
# Due: d2 = 6, m2 = 6, y2 = 2015
# Because y2 = y1, we know it is less than a year late.
# Because m2 = m1, we know it's less than a month late.
# Because d2 < d1, we know that it was returned late (but still within the same month and year).
#
# Per the library's fee structure, we know that our fine will be 15 Hackos * (# days late). We then print the result of 15 * (d1 - d2) = 15 * (9 - 6) = 45 as our output.


# Solution 1
def libraryFine(d1, m1, y1, d2, m2, y2):
    total = 0

    # Checking for the year
    if y1 > y2:
        total = 10000
    # Checking for the month
    elif y1 == y2 and m1 > m2:
        total = 500 * (m1 - m2)
    # Checking for the day
    elif y1 == y2 and m1 == m2 and d1 > d2:
        total = 15 * (d1 - d2)

    return total


# Solution 2
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    elif y1 == y2:
        if m1 > m2:
            return 500 * (m1 - m2)
        elif m1 == m2:
            if d1 > d2:
                return 15 * (d1 - d2)
            else:
                return 0
        else:
            return 0
    else:
        return 0
