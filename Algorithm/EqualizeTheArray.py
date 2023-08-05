# Given an array of integers, determine the minimum number of elements to delete to leave only elements of equal value.

# Example
# ar = [1, 2, 2, 3]
# Delete the 2 elements 1 and 3 leaving arr = [2, 2]. If both twos plus either the 1 or the 3 are deleted, it takes 3 deletions to leave either [3] or [1]. The minimum number of deletions is 2.

# Return an integer representing the minimum number of deletions needed to make all elements equal.

# Sample Input 0
# 5
# 3 3 2 1 3

# Sample Output 0
# 2

# Explanation 0
# The array ar = [3, 3, 2, 1, 3]. If we delete arr[2] = 2 and arr[3] = 1, all of the elements in the resulting array, A' = [3, 3, 3], will be equal. Deleting these 2 elements is minimal. Our only other options would be to delete 4 elements to get an array of either [1] or [2].

# Sample Input 1
# 5
# 4 5 5 4 2

# Sample Output 1
# 2

# Explanation 1
# Removing ar[0] = 4 and ar[3] = 4 gives ar' = [5, 5, 2]. Deleting any fewer than 2 elements leaves us with at least one 5 and one 2.


# Solution 1


def equalizeArray(arr):
    # Find the maximum element in the array
    # eg. [1, 2, 2, 3] -> 3
    l = max(arr)
    # Create a list of length l with all elements as 0
    # eg. [0, 0, 0]
    c = [0] * l

    # Iterate through the array
    for i in arr:
        # Increment the count of the element in the array
        c[i - 1] += 1

    # c = [1, 2, 1]

    # Find the maximum element in the array
    maxim = max(c)

    return sum(c) - maxim


# Solution 2
def equalizeArray(arr):
    # Write your code here
    count = 0

    # Iterate through the array
    for i in range(len(arr)):
        # Count the number of times the current element appears in the array
        # If the count is greater than the current count, update the count to the current count
        # eg. [1, 2, 2, 3] -> 2 appears twice, 3 appears once, 1 appears once
        # 1st iteration , i =0, arr.count(arr[0]) = 1, count = 0, count = 1
        if arr.count(arr[i]) > count:
            # Update the count to the current count
            # 2nd iteration, i = 1, arr.count(arr[1]) = 2, count = 1, count = 2

            count = arr.count(arr[i])

    # Return the length of the array minus the count
    return len(arr) - count


# Solution 3 - Using Dictionary
def equalizeArray(arr):
    # Write your code here
    # Create an empty dictionary
    d = {}

    # Iterate through the array
    for i in arr:
        # If the element is not in the dictionary, add it to the dictionary
        # eg. [1, 2, 2, 3] -> {1: 1}
        # 2nd iteration, i = 2, 2 is in the dictionary, increment the count of 2 by 1
        # 3rd iteration, i = 2, 2 is in the dictionary, increment the count of 2 by 1
        # 4th iteration, i = 3, 3 is not in the dictionary, add 3 to the dictionary
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    # Find the maximum value in the dictionary
    # eg. {1: 1, 2: 2, 3: 1} -> 2
    maxim = max(d.values())

    # Return the length of the array minus the maximum value
    return len(arr) - maxim


# Solution 4 - Using Counter
from collections import Counter


def equalizeArray(arr):
    # Write your code here
    # Create a counter object
    count = Counter(arr)

    # Return the length of the array minus the most common element
    return len(arr) - count.most_common(1)[0][1]


# Input
arr = [1, 2, 2, 3]
print(equalizeArray(arr))
