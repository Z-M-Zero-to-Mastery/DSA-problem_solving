# Given a 6*6 2D Array, :

    # 1 1 1 0 0 0
    # 0 1 0 0 0 0
    # 1 1 1 0 0 0
    # 0 0 0 0 0 0
    # 0 0 0 0 0 0
    # 0 0 0 0 0 0

# An hourglass in A is a subset of values with indices falling in this pattern in arr's graphical representation:

    # a b c
    #   d
    # e f g

# There are 16 hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum. The array will always be 6*6.

# Example
# arr = 
    # -9 -9 -9  1 1 1 
    #  0 -9  0  4 3 2
    # -9 -9 -9  1 2 3
    #  0  0  8  6 6 0
    #  0  0  0 -2 0 0
    #  0  0  1  2 4 0

# The 16 hourglass sums are:
    # -63, -34, -9, 12, 
    # -10,   0, 28, 23, 
    # -27, -11, -2, 10, 
    #   9,  17, 25, 18

# The highest hourglass sum is 28 from the hourglass beginning at row 1, column 2:

# Solution:

def hourglassSum(arr):
    max_sum = -63
    for i in range(4):
        for j in range(4):
            sum = 0
            sum += arr[i][j] + arr[i][j+1] + arr[i][j+2]
            sum += arr[i+1][j+1]
            sum += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            max_sum = max(max_sum, sum)
    return max_sum

# Time Complexity: O(1)
# Space Complexity: O(1)

def hourglassSum(arr):
    maxSum = -99

# loop through the 2D array
# The range is 4 the hourglass is 3*3
# The last hourglass starts at arr[3][3]
    for i in range(4):
        # The range is 4 the because the hour glass occure in 6*6 matrix (36) is 4*4 (16)
        for j in range(4):

            # sum the top of hourglass
            top = sum(arr[i][j:j+3])
            # sum the mid of hourglass
            mid = arr[i+1][j+1]
            # sum the bottom of hourglass
            bottom = sum(arr[i+2][j:j+3])
            # sum the total of hourglass
            hourglass = top + mid + bottom
            # compare the sum of hourglass with maxSum
            maxSum = max(hourglass, maxSum)
    
    # return the maxSum
    return maxSum
