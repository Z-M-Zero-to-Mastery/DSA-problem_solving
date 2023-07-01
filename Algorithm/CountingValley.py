# An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly step steps, for every step it was noted if it was an uphill, U, or a downhill, D step. Hikes always start and end at sea level, and each step up or down represents a 1 unit change in altitude. We define the following terms:

# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

# Example
# steps = 8 path = [DDUUUUDD]
# The hiker first enters a valley 2 units deep. Then they climb out and up onto a mountain 2 units high. Finally, the hiker returns to sea level and ends the hike.

# Return
# int: the number of valleys traversed

# Sample Input
# 8
# UDDDUDUU

# Sample Output
# 1

# Explanation
# If we represent _ as sea level, a step up as /, and a step down as \, the hike can be drawn as:

# _/\      _
#    \    /
#     \/\/

# The hiker enters and leaves one valley.


# Solution 1:
# Time Complexity: O(n)
# Space Complexity: O(1)
def countingValleys(n, s):
    # Write your code here
    count = 0
    valley = 0

    # UDDDUDUU
    for i in range(n):
        if s[i] == "U":
            count += 1
        else:
            count -= 1
        if count == 0 and s[i] == "U":
            valley += 1

    return valley


# Solution 2: Using Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
def countingValleys(n, s):
    # Write your code here
    stack = []
    valley = 0
    for i in range(n):
        if len(stack) == 0:
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.append(s[i])
        else:
            stack.pop()
            if len(stack) == 0 and s[i] == "U":
                valley += 1
    return valley


# Solution 3: Using Dictionary
# Time Complexity: O(n)
# Space Complexity: O(n)


def countingValleys(n, s):
    # Write your code here
    valleyCount = level = 0

    d = {"U": 1, "D": -1}

    for step in s:
        level += d[step]

        if level == 0 and step == "U":
            valleyCount += 1

    return valleyCount


# Input
n = 8
s = "UDDDUDUU"

print(countingValleys(n, s))
