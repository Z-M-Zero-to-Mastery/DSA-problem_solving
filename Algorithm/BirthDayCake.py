# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

# Example
# candles = [4,4,1,3]
# The maximum height candles are 4 units high. There are 2 of them, so return 2.


# Solution 1:
def birthdayCakeCandles(candles):
    max_height = max(candles)
    return candles.count(max_height)


# Solution 2:
def birthdayCakeCandles(candles):
    maxNum = 0
    count = 0
    n = len(candles)

    for i in range(n):
        if candles[i] > maxNum:
            # Finding the maximum number
            maxNum = candles[i]
            count = 0
        # Counting the number of times the maximum number occurs
        if candles[i] == maxNum:
            count += 1

    return count


# Solution 3:
def birthdayCakeCandles(candles):
    maxVal = 0
    dicto = {}

    for i in range(len(candles)):
        if maxVal < candles[i]:
            maxVal = candles[i]

        if candles[i] in dicto:
            dicto[candles[i]] += 1
        else:
            dicto[candles[i]] = 1

    return dicto[maxVal]


# Input
# 4
# 3 2 1 3
candles = [3, 2, 1, 3]
print(birthdayCakeCandles(candles))
