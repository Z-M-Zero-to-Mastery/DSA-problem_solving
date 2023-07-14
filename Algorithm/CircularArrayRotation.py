# John Watson knows of an operation called a right circular rotation on an array of integers. One rotation operation moves the last array element to the first position and shifts all remaining elements right one. To test Sherlock's abilities, Watson provides Sherlock with an array of integers. Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.
#
# For each array, perform a number of right circular rotations and return the values of the elements at the given indices.

# Example
# a = [3,4,5]
# k = 2
# queries = [1,2]

# Here k is the number of rotations on a, and queries holds the list of indices to report. First we perform the two rotations:
# [3,4,5] -> [5,3,4] -> [4,5,3]

# Now return the values from the zero-based indices 1 and 2 as indicated in the queries array.
# a[1] = 5
# a[2] = 3

# Return an array with the values [5,3].

# Sample Input 0
# 3 2 3
# 1 2 3
# 0
# 1
# 2

# Sample Output 0
# 2
# 3
# 1

# Explanation 0
# After the first rotation, the array becomes [3,1,2].
# After the second (and final) rotation, the array becomes [2,3,1]. We then print the values of the zero-based indices 2, 3, and 1 which are 2, 3, and 1.

# Sample Input 1
# 3 3 4
# 1 2 3
# 0
# 1
# 2
# 3

# Sample Output 1
# 2
# 3
# 1
# 2

# Explanation 1
# After the first rotation, the array becomes [3,1,2].
# After the second rotation, the array becomes [2,3,1].
# After the third rotation, the array becomes [1,2,3].
# After the fourth rotation, the array becomes [3,1,2].
# We then print the values of the zero-based indices 2, 3, and 1 which are 2, 3, and 1.


# Solution 1
def circularArrayRotation(a, k, queries):
    res = []
    n = len(a)
    # It is not necessary to rotate the array k times if k > n because the result will be the same as rotating k % n times only (k % n < n) and k % n < n <==> k < n (k is an integer) so we can just do k = k % n to reduce the number of rotations. For example, if we have an array of 3 elements [1, 2, 3] and we rotate it 4 times, the result will be the same as rotating it 1 time only (4 % 3 = 1) so we can just do
    k = k % n
    # print(n)

    # This loop is to fetch the values at the given indices
    for q in queries:
        # It will append the values at the given indices to the res array
        # (n - k + q) % n is the new index of the element at the given index q after k rotations
        # eg : if we have an array of 3 elements [1, 2, 3] and we rotate it 2 times, the new index of the element at index 1 (value 2) will be (3 - 2 + 1) % 3 = 2 % 3 = 2 (the new index of 2 is 2)
        res.append(a[(n - k + q) % n])

    return res


# Solution 2
def circularArrayRotation(a, k, queries):
    # Write your code here
    for i in range(k):
        # pop the last element and insert it at the beginning
        a.insert(0, a.pop())
    # return the values at the given indices
    return [a[i] for i in queries]


# Solution 3
def circularArrayRotation(a, k, queries):
    # Write your code here
    # create a new array
    new_arr = []
    # iterate through the array
    for i in range(len(a)):
        # calculate the new index
        new_index = (i + k) % len(a)
        # insert the value at the new   index
        new_arr.insert(new_index, a[i])
    # return the values at the given indices
    return [new_arr[i] for i in queries]


# Input
a = [3, 4, 5]
k = 2
queries = [1, 2]
print(circularArrayRotation(a, k, queries))
