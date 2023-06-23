# Given an array of integers and a positive integer k, determine the number of (i, j) pairs where i < j and ar[i] + ar[j] is divisible by k.

# Example
# ar = [1, 2, 3, 4, 5, 6]
# k = 5
# Three pairs meet the criteria: [1, 4], [2, 3] and [4, 6].

# Sample Input
# 6 3
# 1 3 2 6 1 2

# Sample Output
# 5

# Explanation
# Here are the 5 valid pairs when k = 3:
# (0, 2) -> ar[0] + ar[2] = 1 + 2 = 3
# (0, 5) -> ar[0] + ar[5] = 1 + 2 = 3
# (1, 3) -> ar[1] + ar[3] = 3 + 6 = 9
# (2, 4) -> ar[2] + ar[4] = 2 + 1 = 3
# (4, 5) -> ar[4] + ar[5] = 1 + 2 = 3


# Solution 1:
def divisibleSumPairs(n, k, ar):
    count = 0
    # Here loop through the array
    for i in range(n):
        # Here loop through the array again to find the pairs
        # Note: j starts from i+1 to avoid the duplicate pairs
        # eg: (0, 1) and (1, 0)
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count


# Input
n = 6
k = 3
ar = [1, 3, 2, 6, 1, 2]
print(divisibleSumPairs(n, k, ar))
