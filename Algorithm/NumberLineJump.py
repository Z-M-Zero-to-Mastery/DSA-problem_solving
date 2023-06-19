# You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

# The first kangaroo starts at location  and moves at a rate of  meters per jump.
# The second kangaroo starts at location  and moves at a rate of  meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.

# Example
# x1 = 2
# v1 = 1
# x2 = 2
# v2 = 1

# After one jump, they are both at x=3 , (x1+v1 = 1+2 ,x2+v2= 2+1 )=3, so the answer is YES.

# Sample Input 0

# 0 3 4 2
# Sample Output 0

# YES
# Explanation 0

# The two kangaroos jump through the following sequence of locations:

# image

# From the image, it is clear that the kangaroos meet at the same location (number 12 on the number line) after same number of jumps (4 jumps), and we print YES.

# Sample Input 1

# 0 2 5 3
# Sample Output 1

# NO

# Explanation 1

# The second kangaroo has a starting location that is ahead (further to the right) of the first kangaroo's starting location (i.e.,x2 > x1 ). Because the second kangaroo moves at a faster rate (meaning v2 > v1) and is already ahead of the first kangaroo, the first kangaroo will never be able to catch up. Thus, we print NO.

# Solution 1:


def kangaroo(x1, v1, x2, v2):
    # This is to check if the first kangaroo is ahead of the second kangaroo and if the first kangaroo is faster than the second kangaroo
    # ie the velocity of the first kangaroo is greater than the velocity of the second kangaroo
    # eg: x1 = 2, v1 = 3, x2 = 1, v2 = 2

    if v1 > v2:
        # This is to check if the difference between the starting point of the first kangaroo and the second kangaroo is divisible by the difference between the velocity of the first kangaroo and the second kangaroo
        # eg : (1-2)%(3-2) = -1%1 = 0
        if (x2 - x1) % (v1 - v2) == 0:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


# Solution 2:


def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 < v2:
        return "NO"
    else:
        if v1 != v2 and (x2 - x1) % (v1 - v2) == 0:
            return "YES"
        else:
            return "NO"


# Solution 3:


def kangaroo(x1, v1, x2, v2):
    if v1 > v2:
        while x1 < x2:
            x1 += v1
            x2 += v2
        if x1 == x2:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


# Input
# 0 3 4 2
print(kangaroo(0, 3, 4, 2))
