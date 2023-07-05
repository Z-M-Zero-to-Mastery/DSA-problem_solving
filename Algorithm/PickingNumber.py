# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.

# Example
# a = [1,1,2,2,4,4,5,5,5]
# There are two subarrays meeting the criterion: [1,1,2,2] and [4,4,5,5,5]. The maximum length subarray has 5 elements.

# Return an integer representing the length of the longest subarray that meets the criterion.

# Sample Input 0
# 6
# 4 6 5 3 3 1

# Sample Output 0
# 3

# Explanation 0
# We choose the following multiset of integers from the array: {4,3,3}. Each pair in the multiset has an absolute difference <= 1 (i.e., |4-3| = 1 and |3-3| = 0), so we print the number of chosen integers, 3, as our answer.

# Sample Input 1
# 6
# 1 2 2 3 1 2

# Sample Output 1
# 5

# Explanation 1
# We choose the following multiset of integers from the array: {1, 2, 2, 1, 1}. Each pair in the multiset has an absolute difference <= 1 (i.e., |1-2| = 1, |1-1| = 0 and |2-2| = 0), so we print the number of chosen integers, 5, as our answer.

# Solution 1:


def pickingNumbers(a):
    max_count = 0
    for i in a:
        c = a.count(i)
        d = a.count(i - 1)
        c = c + d
        if c > max_count:
            max_count = c
    return max_count


# Solution 2:


def pickingNumbers(a):
    ar = [0] * (max(a) + 1)
    # Iterate through the array and count the number of times each value appears
    for i in a:
        ar[i] += 1
    # eg : a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
    # eg: ar = [0, 2, 2, 0, 2, 3]

    maxVal = 0
    for i in range(len(ar) - 1):
        if ar[i] + ar[i + 1] > maxVal:
            maxVal = ar[i] + ar[i + 1]

    return maxVal


# Input
a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
print(pickingNumbers(a))
