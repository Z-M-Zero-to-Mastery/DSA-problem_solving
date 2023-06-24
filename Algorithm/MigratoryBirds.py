# Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

# Example
# arr = [1,1,2,2,3]
# There are two each of types 1 and 2, and one sighting of type 3. Pick the lower of the two types seen twice: type 1.

# Sample Input
# 6
# 1 4 4 4 5 3

# Sample Output
# 4

# Explanation
# The different types of birds occur in the following frequencies:
# Type 1: 1 bird
# Type 2: 0 birds
# Type 3: 1 bird
# Type 4: 3 birds
# Type 5: 1 bird
# The type number that occurs at the highest frequency is type 4, so we print 4 as our answer.


# Solution 1:
def migratoryBirds(arr):
    # Write your code here
    count = [0] * len(arr)

    # Count the number of each bird type
    # eg. arr = [1,1,2,2,3]
    # count = [0, 2, 2, 1]
    for i in arr:
        count[i] += 1

    # It will return the index of the first max value
    # eg. count = [0, 2, 2, 1]
    # return 1
    # The index function will return the first index of the value
    return count.index(max(count))


# Solution 2: Using dictionary
def migratoryBirds(arr):
    # Write your code here
    count = {}

    # Count the number of each bird type
    # eg. arr = [1,1,2,2,3]
    # count = {1: 2, 2: 2, 3: 1}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    # It will return the key of the max value
    # eg. count = {1: 2, 2: 2, 3: 1}
    # return 1
    return max(count, key=count.get)


# Solution 3: Using Counter
from collections import Counter


def migratoryBirds(arr):
    # Write your code here
    count = Counter(arr)

    # It will return the key of the max value
    # eg. count = {1: 2, 2: 2, 3: 1}
    # return 1
    return max(count, key=count.get)


# Input
arr = [1, 1, 2, 2, 3]

print(migratoryBirds(arr))
