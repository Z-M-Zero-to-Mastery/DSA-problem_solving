# Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

# Example
# n = 10
# queries = [[1,5,3],[4,8,7],[6,9,1]]

# Queries are interpreted as follows:
# a b k
# 1 5 3
# 4 8 7
# 6 9 1
# Add the values of  between the indices  and  inclusive:

# index->	 1 2 3  4  5 6 7 8 9 10
# [0,0,0, 0, 0,0,0,0,0, 0]
# [3,3,3, 3, 3,0,0,0,0, 0]
# [3,3,3,10,10,7,7,7,0, 0]
# [3,3,3,10,10,8,8,8,1, 0]

# The largest value is 10 after all operations are performed.
#  Sample Input
# 5 3
# 1 2 100
# 2 5 100
# 3 4 100
# Explanation
# After the first update the list is 100 100 0 0 0.
# After the second update list is 100 200 100 100 100.
# After the third update list is 100 200 200 200 100.
# The maximum value is 200.

# **************************************************************************
# def arrayManipulation(n, queries):
# Write your code here
# arr = [0]*n
# # print(queries)
# for i in queries:
#     for j in range(i[0]-1, i[1]):
#         arr[j] += i[2]

# return max(arr)

# This is a brute force approach which will not work for large inputs
# **************************************************************************


# Solution 1:
def arrayManipulation(n, queries):
    # Here we are using prefix sum algorithm
    #  we are adding n+2 elements in the array because we are adding k at index a and subtracting k at index b+1
    # so that we can get the sum of all the elements from index 1 to n
    arr = [0] * (n + 2)

    for a, b, k in queries:
        # here we are adding k at index a and subtracting k at index b+1
        arr[a] += k
        arr[b + 1] -= k

    maxVal = temp = 0
    #  This is the prefix sum algorithm
    # we are adding the elements from index 1 to n and storing the maximum value in maxVal
    # temp is used to store the sum of all the elements from index 1 to n
    # eg : arr = [0, 3, 0, 0, -3]
    # temp = 0
    # maxVal = 0
    # temp = 0 + 3 = 3
    # maxVal = max(0, 3) = 3
    # temp = 3 + 0 = 3
    # maxVal = max(3, 3) = 3
    # temp = 3 + 0 = 3
    # maxVal = max(3, 3) = 3
    # temp = 3 + (-3) = 0
    # maxVal = max(3, 0) = 3
    # so the maximum value is 3
    for val in arr:
        temp += val
        maxVal = max(maxVal, temp)

    return maxVal


# Solution 2:
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for a, b, k in queries:
        arr[a - 1] += k
        if b < n:
            arr[b] -= k
    maxVal = temp = 0
    for val in arr:
        temp += val
        maxVal = max(maxVal, temp)
    return maxVal


# Solution 3:
# using dictionary
def arrayManipulation(n, queries):
    arr = {}

    for a, b, k in queries:
        arr[a] = arr.get(a, 0) + k
        arr[b + 1] = arr.get(b + 1, 0) - k

    maxVal = temp = 0
    for i in sorted(arr)[:-1]:
        temp += arr[i]
        maxVal = max(maxVal, temp)

    return maxVal
