# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix arr is shown below:

    # 1 2 3
    # 4 5 6
    # 9 8 9  

# The left-to-right diagonal 1+5+9 = 15 . The right to left diagonal 3+5+9 = 17. Their absolute difference is |15 - 17| = 2.

# Solution 1:

def diagonalDifference(arr):
    size = len(arr)

    left = right = 0

    for i in range(size):
        # It will take value from left to right
        left += arr[i][i]
        # It will take value from right to left
        right += arr[i][size-1-i]

    return abs(left - right)

# Solution 2:

def diagonalDifference(arr):
    size = len(arr)

    leftToRight = sum([arr[i][i] for i in range(size)])
    rightToLeft = sum([arr[i][size-1-i] for i in range(size)])

    return abs(leftToRight - rightToLeft)

# Solution 3:

def diagonalDifference(arr):
    size = len(arr) - 1

#   Calaculate the left to right diagonal
    leftToRight = 0
    i = 0
    exit = True

    while exit:
        # Taking the value from left to right and adding it to the leftToRight variable
        leftToRight += arr[i][i]
        i += 1
        # If i is equal to the size of the array, then exit the loop
        if i == size:
            exit = False

#   Calaculate the right to left diagonal
    rightToLeft = 0
    i = 0
    j = size
    exit = True

    while exit:
        rightToLeft += arr[i][j]
        i += 1
        j -= 1

        if i == size:
            exit = False

    return abs(leftToRight - rightToLeft)


# Input:
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

diagonalDifference(arr)