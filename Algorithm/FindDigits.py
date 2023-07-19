# An integer d is a divisor of an integer n if the remainder of n / d = 0.

# Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.

# Note: Each digit is considered to be unique, so each occurrence of the same digit should be counted (e.g. for n = 111, 1 is a divisor of 111 each time it occurs so the answer is 3).
# Example
# n = 124
# Check whether 1, 2 and 4 are divisors of 124. All 3 numbers divide evenly into 124 so return 3.
# n = 111
# Check whether 1, 1, and 1 are divisors of 111. All 3 numbers divide evenly into 111 so return 3.
# n = 10
# Check whether 1 and 0 are divisors of 10. 1 is, but 0 is not. Return 1.

# Return the number of digits in n that are divisors of n.


# Solution:
def findDigits(n):
    count = 0

    # convert n to string and iterate through each digit
    for i in str(n):
        # check if digit is not 0 and if n is divisible by digit
        if int(i) != 0 and n % int(i) == 0:
            count += 1

    return count


print(findDigits(124))  # 3
