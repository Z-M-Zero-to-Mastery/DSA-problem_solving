# Given a set of distinct integers, print the size of a maximal subset of S where the sum of any 2 numbers in S is not evenly divisible by k.

# Example
# S = [19, 10, 12, 10, 24, 25, 22]
# k = 4
# One of the arrays that can be created is S'[0] = [10, 12, 25]. Another is S'[1] = [19, 22, 24]. After testing all permutations, the maximum length solution array has 3 elements.

# Function Description : Complete the nonDivisibleSubset function in the editor below. It should return an integer representing the length of the longest subset of S meeting the criteria.

# Return the length of the largest possible subset.

# Sample Input
# 4 3
# 1 7 2 4

# Sample Output
# 3

# Explanation
# The sums of all permutations of two elements from S = {1, 7, 2, 4} are:
# 1 + 7 = 8
# 1 + 2 = 3
# 1 + 4 = 5
# 7 + 2 = 9
# 7 + 4 = 11
# 2 + 4 = 6
# We see that only S' = {1, 7, 4} will not ever sum to a multiple of k = 3.


# Solution  : Optimized
# Time Complexity : O(n)
# Space Complexity : O(n)
# Count the frequency of each remainder when divided by k
# If remainder is 0, then there can be only one such element in the set
# If remainder is k/2, then there can be only one such element in the set
# For all other remainders, the maximum number of elements that can be in the set is the maximum of the frequency of the remainder and the frequency of k - remainder


def nonDivisibleSubset(k, s):
    # Count the number of times each number in s is divisible by k.
    reminder = [0] * k
    for num in s:
        # The remainder of the number when divided by k is calculated. The count of the remainder is incremented.
        reminder[num % k] += 1
    # eg : s = [1, 7, 2, 4] and k = 3
    # reminder = [1, 2, 1]

    # The size of the largest subset is the number of times the numbers in the
    # subset are divisible by k. If k is even, then the largest subset can
    # contain at most 1 number divisible by k.
    # If k is odd, then the largest subset can contain at most 1 number divisible by k and 1 number divisible by k/2.
    # eg : k = 3
    # result = min(reminder[0], 1) = min(1, 1) = 1
    # eg : k = 4
    # result = min(reminder[0], 1) = min(1, 1) = 1
    result = min(reminder[0], 1)

    # This loop iterates over the first half of the reminder array. The second half of the array is not iterated over because the second half of the array is the same as the first half.
    # here k // 2 + 1 is used because range() is exclusive of the second argument.
    # eg : k = 3 , range(1, 2) = [1]
    for i in range(1, k // 2 + 1):
        # It checks if the remainder is 0 or k/2. If it is, then the number of elements in the subset is 1.
        # eg : k = 3, i = 1 , 1 != 3 - 1 = 2 , result = 1 + max(reminder[1], reminder[2]) = 1 + max(2, 1) = 3
        if i != k - i:
            result += max(reminder[i], reminder[k - i])

    # If k is even, then the largest subset can contain at most 1 number divisible by k.
    # eg : k = 4, 4 % 2 = 0 , result = 3 + 1 = 4
    if k % 2 == 0:
        result += 1

    return result
