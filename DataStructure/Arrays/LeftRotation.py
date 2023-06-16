# A left rotation operation on an array of size n shifts each of the array's elements 1 unit to the left. Given an integer,d , rotate the array that many steps left and return the result.

# Example
# d = 2
# arr = [1,2,3,4,5]
# after 2 rotations, arr' = [3,4,5,1,2]

# Solution 1:


def rotLeft(a, d):
    for i in range(d):
        a.append(a.pop(0))
    return a


# Solution 2:


def rotLeft(a, d):
    return a[d:] + a[:d]


# Input
# 5 4
# 1 2 3 4 5

rotLeft([1, 2, 3, 4, 5], 4)
