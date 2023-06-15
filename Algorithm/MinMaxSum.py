# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Input Format
# A single line of five space-separated integers.

# Example
# arr = [1,3,5,7,9]
# The minimum sum is 1+3+5+7=16 and the maximum sum is 3+5+7+9=24. The function prints
# 16 24

# Explanation
# Our initial numbers are 1,3,5,7, and 9. We can calculate the following sums using four of the five integers:
# 1. If we sum everything except 1, our sum is 3+5+7+9=24.
# 2. If we sum everything except 3, our sum is 1+5+7+9=22.
# 3. If we sum everything except 5, our sum is 1+3+7+9=20.
# 4. If we sum everything except 7, our sum is 1+3+5+9=18.
# 5. If we sum everything except 9, our sum is 1+3+5+7=16.


# Solution 1:
def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[: len(arr) - 1]), sum(arr[1:]))


# Solution 2:
def miniMaxSum(arr):
    print(sum(arr) - max(arr), sum(arr) - min(arr))


# Solution 3:
def miniMaxSum(arr):
    minVal = 999999999
    maxVal = 0
    sumVal = 0
    n = len(arr)

    for i in range(n):
        sumVal += arr[i]

        if arr[i] < minVal:
            minVal = arr[i]

        if arr[i] > maxVal:
            maxVal = arr[i]

    print(sumVal - maxVal, sumVal - minVal)


# Input:
# 1 2 3 4 5
arr = [1, 2, 3, 4, 5]
miniMaxSum(arr)
