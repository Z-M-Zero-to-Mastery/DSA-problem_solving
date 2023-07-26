# You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, discarding the shortest pieces until there are none left. At each iteration you will determine the length of the shortest stick remaining, cut that length from each of the longer sticks and then discard all the pieces of that shortest length. When all the remaining sticks are the same length, they cannot be shortened so discard them.

# Given the lengths of n sticks, print the number of sticks that are left before each iteration until there are none left

# Example
# arr = [1,2,3]
# The shortest stick length is 1, so cut that length from the longer two and discard the pieces of length 1. Now the lengths are arr = [1,2]. Again, the shortest stick is of length 1, so cut that amount from the longer stick and discard those pieces. There is only one stick left, arr = [1], so discard that stick. The number of sticks at each iteration are answer = [3,2,1].

# Returns : int[]: the number of sticks after each iteration

# Sample Input 0 :
# 6
# 5 4 4 2 2 8

# Sample Output 0 :
# 6
# 4
# 2
# 1

# Explanation 0 :
# sticks-length        length-of-cut   sticks-cut
# 5 4 4 2 2 8             2               6
# 3 2 2 _ _ 6             2               4
# 1 _ _ _ _ 4             1               2
# _ _ _ _ _ 3             3               1
# _ _ _ _ _ _           DONE            DONE

# Sample Input 1 :
# 8
# 1 2 3 4 3 3 2 1

# Sample Output 1 :
# 8
# 6
# 4
# 1

# Explanation 1 :
# sticks-length         length-of-cut   sticks-cut
# 1 2 3 4 3 3 2 1         1               8
# _ 1 2 3 2 2 1 _         1               6
# _ _ 1 2 1 1 _ _         1               4
# _ _ _ 1 _ _ _ _         1               1
# _ _ _ _ _ _ _ _       DONE            DONE


# Solution 1 :
def cutTheSticks(arr):
    result = []

    while len(arr) > 0:
        result.append(len(arr))

        # This list comprehension is used to subtract the minimum value from each element in the list
        # and then remove all the elements that are less than or equal to 0 from the list
        # eg : arr = [1,2,3,4,5] => [0,1,2,3,4] => [1,2,3,4]
        arr = [x - min(arr) for x in arr if x - min(arr) > 0]
        # The above list comprehension is equivalent to the following code
        # for x in arr:
        #     if x - min(arr) > 0:
        #         arr.append(x - min(arr))

    return result


# Solution 2 : Using Counter
from collections import Counter


def cutTheSticks(arr):
    result = []
    # Counter returns a dictionary with the number of occurences of each element in the list
    # eg : arr = [1,2,3,4,5] => {1:1, 2:1, 3:1, 4:1, 5:1}
    count = Counter(arr)

    # sorted(count) returns a list of all the keys in the dictionary in sorted order
    for i in sorted(count):
        # The number of sticks remaining after each iteration is the length of the list
        result.append(len(arr))
        # The number of sticks cut in each iteration is the value of the key in the dictionary
        # eg : count[1] = 1, count[2] = 1, count[3] = 1, count[4] = 1, count[5] = 1
        # eg : count[1] = 2, count[2] = 1, count[3] = 3, count[4] = 1, count[5] = 1
        arr = arr[count[i] :]

    return result


# Solution 3 : Using dictionary
def cutTheSticks(arr):
    result = []
    # Create an empty dictionary
    count = {}

    # Iterate through the list and add the elements to the dictionary
    for i in arr:
        # If the element is already present in the dictionary, increment the value by 1
        if i in count:
            count[i] += 1
        # If the element is not present in the dictionary, add it to the dictionary and set the value to 1
        else:
            count[i] = 1

    # sorted(count) returns a list of all the keys in the dictionary in sorted order
    for i in sorted(count):
        # The number of sticks remaining after each iteration is the length of the list
        result.append(len(arr))
        # The number of sticks cut in each iteration is the value of the key in the dictionary
        # eg : count[1] = 1, count[2] = 1, count[3] = 1, count[4] = 1, count[5] = 1
        # eg : count[1] = 2, count[2] = 1, count[3] = 3, count[4] = 1, count[5] = 1
        arr = arr[count[i] :]

    return result


# Solution 4 : Using set
def cutTheSticks(arr):
    result = []
    # Create an empty set
    count = set()

    # Iterate through the list and add the elements to the set
    for i in arr:
        count.add(i)

    # sorted(count) returns a list of all the elements in the set in sorted order
    for i in sorted(count):
        # The number of sticks remaining after each iteration is the length of the list
        result.append(len(arr))
        # The number of sticks cut in each iteration is the number of times the element is present in the list
        # eg : arr = [1,2,3,4,5] => 1 is present 1 time, 2 is present 1 time, 3 is present 1 time, 4 is present 1 time, 5 is present 1 time
        # eg : arr = [1,2,3,4,5] => 1 is present 2 times, 2 is present 1 time, 3 is present 3 times, 4 is present 1 time, 5 is present 1 time

        arr = arr.count(i)

    return result


# Input
arr = [1, 2, 3, 4, 3, 3, 2, 1]
print(cutTheSticks(arr))
