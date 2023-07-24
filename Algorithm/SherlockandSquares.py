# Watson likes to challenge Sherlock's math ability. He will provide a starting and ending value that describe a range of integers, inclusive of the endpoints. Sherlock must determine the number of square integers within that range.
# Note: A square integer is an integer which is the square of an integer, e.g. 1,4,9,16,25.

# Example
# a = 24
# b = 49
# There are three square integers in the range: 25,36 and 49. Return 3.

# Function Description
# Complete the squares function in the editor below. It should return an integer representing the number of square integers in the inclusive range from a to b.
# squares has the following parameter(s):
# - int a: the lower range boundary
# - int b: the upper range boundary

# Returns : int: the number of square integers in the range

# Sample Input
# 2
# 3 9
# 17 24

# Sample Output
# 2
# 0

# Explanation
# Test Case #00: In range [3,9], 4 and 9 are the two square integers.
# Test Case #01: In range [17,24], there are no square integers.

# Solution 1 (Brute Force)
import math
import os


def squares(a, b):
    count = 0
    for i in range(a, b + 1):
        if math.sqrt(i) == int(math.sqrt(i)):
            count += 1

    return count


# Solution 2 (Optimized)
def squares(a, b):
    # It is enough to find the square root of the first and last number in the range and round them up and down respectively.
    # eg : a = 24, b = 49
    # sqrt(49) = 7, floor(7) = 7
    # sqrt(24) = 4.89, ceil(4.89) = 5
    # So the number of square integers in the range is 7 - 5 + 1 = 3
    return math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1


# Input
a = 3
b = 9

print(squares(a, b))
