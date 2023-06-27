# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# Example
# n = 7
# ar = [1, 2, 1, 2, 1, 3, 2]

# There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.


# Solution 1:
def sockMerchant(n, ar):
    count = 0
    d = {}

    for i in ar:
        d[i] = d.get(i, 0) + 1

    for i in d.keys():
        count += d[i] // 2

    return count


# Solution 2:
def sockMerchant(n, ar):
    pair = 0

    for i in range(len(ar)):
        for j in range(i + 1, len(ar)):
            if ar[i] == ar[j]:
                ar.pop(j)
                pair += 1
                break

    return pair


# Solution 3: (Using Counter)
from collections import Counter


def sockMerchant(n, ar):
    count = 0
    for i in Counter(ar).values():
        count += i // 2
    return count


# Solution 4:
def sockMerchant(n, ar):
    count = 0

    # set() returns unique values
    # eg: set([1, 2, 1, 2, 1, 3, 2]) = {1, 2, 3}
    # And we iterate through the set and count the number of pairs
    for i in set(ar):
        # ar.count(i) returns the number of occurences of i in ar
        # eg: ar.count(1) = 3
        count += ar.count(i) // 2
    return count


# Solution 5:
def sockMerchant(n, ar):
    count = 0
    ar.sort()

    # ar = [1, 1, 1, 2, 2, 3, 2]
    # i = 0, 1, 2, 3, 4, 5, 6
    # ar[i] = 1, 1, 1, 2, 2, 2, 3
    # ar[i] == ar[i + 1] => count += 1, 2, 3
    for i in range(n - 1):
        if ar[i] == ar[i + 1]:
            count += 1
            i += 1
    return count


# Input
n = 7
ar = [1, 2, 1, 2, 1, 3, 2]
print(sockMerchant(n, ar))
