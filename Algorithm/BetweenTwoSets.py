# There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

# Example
# a = [2, 6]
# b = [24, 36]
# There are two numbers between the arrays: 6 and 12.
# 6 % 2 = 0, 6 % 6 = 0, 24 % 6 = 0 and 36 % 6 = 0 for the first value.
# Similarly, 12 % 2 = 0, 12 % 6 = 0 and 24 % 12 = 0, 36 % 12 = 0.

# Sample Input
# 2 3
# 2 4
# 16 32 96

# Sample Output
# 3

# Explanation
# 2 and 4 divide evenly into 4, 8, 12 and 16.
# 4, 8 and 16 divide evenly into 16, 32, 96.
# 4, 8 and 16 are the only three numbers for which each element of a is a factor and each is a factor of all elements of b.

# ************************************************************************

#   We can solve this problem by using the following steps:
#   1. Find the LCM of all the integers of array A.
#   2. Find the GCD of all the integers of array B.
#   3. Count the number of multiples of LCM that evenly divides the GCD.

#   The number that we are choosing must be the common multiple of all the integers of array A.
#   The number that we are choosing must be the factor of all the integers of array B.

# ************************************************************************

# Solution 1: Using GCD and LCM

# Time Complexity: O(n)
# Space Complexity: O(1)

import math


def getTotalX(a, b):
    # Here we are finding the LCM of all the integers of array A.
    # We are taking the first element of array A as the initial value of LCM.
    # eg : a = [2, 6] , b = [24, 36]
    # lcm = 2
    lcm = a[0]
    # We are finding the GCD of all the integers of array B.
    # gcd = 24
    gcd = b[0]

    # We are finding the LCM of all the integers of array A.
    # We are using the formula: LCM(a, b) = a*b / GCD(a, b)
    # eg : a = [2, 6] , b = [24, 36]
    for i in range(1, len(a)):
        # lcm = 2*6 / gcd(2, 6) = 6 In the next iteration, lcm = 6*6 / gcd(6, 6) = 6
        lcm = lcm * a[i] // math.gcd(lcm, a[i])

    # We are finding the GCD of all the integers of array B.
    # eg : a = [2, 6] , b = [24, 36]
    # gcd = gcd(24, 36) = 12
    for i in range(1, len(b)):
        gcd = math.gcd(gcd, b[i])

    # We are counting the number of multiples of LCM that evenly divides the GCD.

    count = 0
    # We are finding the multiples of LCM that evenly divides the GCD.
    # eg : a = [2, 6] , b = [24, 36]
    # Here lcm = 6 and gcd = 12 , the loop will run from 6 to 12 with a step of 6.
    for i in range(lcm, gcd + 1, lcm):
        # Here we are checking if the multiples of LCM evenly divides the GCD.
        if gcd % i == 0:
            count += 1

    return count


# Solution 2: Using GCD and LCM


def getTotalX(a, b):
    # Here we are finding the LCM of all the integers of array A.
    def gcd(a, b):
        #
        if b == 0:
            return a
        # It will recursively call the function gcd with the value of b and a%b.
        # eg : a = [2, 6] , b = [24, 36]
        # gcd(2, 6) = gcd(6, 2) = gcd(2, 0) = 2
        #
        return gcd(b, a % b)

    # Here we are finding the GCD of all the integers of array B.
    def lcm(a, b):
        return a * b // gcd(a, b)

    lcm_a = a[0]
    gcd_b = b[0]

    for i in range(1, len(a)):
        lcm_a = lcm(lcm_a, a[i])

    for i in range(1, len(b)):
        gcd_b = gcd(gcd_b, b[i])

    count = 0
    for i in range(lcm_a, gcd_b + 1, lcm_a):
        if gcd_b % i == 0:
            count += 1

    return count


# Input

print(getTotalX([2, 6], [24, 36]))
