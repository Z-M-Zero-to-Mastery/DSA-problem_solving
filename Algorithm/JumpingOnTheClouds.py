# There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

# For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.
# Example
# c = [0,1,0,0,0,1,0]
# Index the array from 0...6. The number on each cloud is its index in the list so the player must avoid the clouds at indices 1 and 5. They could follow these two paths: 0->2->4->6 or 0->2->3->4->6. The first path takes 3 jumps while the second takes 4. Return 3.

# Return the minimum number of jumps required, as an integer.

# Sample Input 0
# 7
# 0 0 1 0 0 1 0

# Sample Output 0
# 4

# Explanation 0:
# The player must avoid c[2] and c[5]. The game can be won with a minimum of 4 jumps:

# Sample Input 1
# 6
# 0 0 0 0 1 0

# Sample Output 1
# 3

# Explanation 1:
# The only thundercloud to avoid is c[4]. The game can be won in 3 jumps:


# Solution: 1 - Brute Force
# Time Complexity: O(n)
# Space Complexity: O(1)
def jumpingOnClouds(c):
    i = 0
    jumps = 0

    # Here we are looping through the array and checking if the next two elements are 0 or not. If they are 0, we are incrementing the index by 2 and if not, we are incrementing the index by 1. We are also incrementing the jumps by 1 in both the cases.
    # len(c) - 1 is used because we are checking the next two elements. If we don't use len(c) - 1, we will get an index out of range error.
    while i < len(c) - 1:
        # Here we are checking if the next two elements are 0 or not. If they are 0, we are incrementing the index by 2 and if not, we are incrementing the index by 1. We are also incrementing the jumps by 1 in both the cases.
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2

        # In else, we are incrementing the index by 1 and jumps by 1.
        else:
            i += 1

        # Here we are incrementing the jumps by 1. This is done in both the cases.
        jumps += 1

    return jumps


# Solution: 2 - Recursion
# Time Complexity: O(n)
# Space Complexity: O(n)
def jumpingOnClouds(c):
    # Here we are defining a function called jump which takes an index as an argument.
    def jump(i):
        # Here we are checking if the index is greater than or equal to the length of the array. If it is, we are returning 0.
        if i >= len(c) - 1:
            return 0
        # Here we are checking if the element at the index is 1. If it is, we are returning infinity.
        if c[i] == 1:
            return float("inf")

        # Here we are returning 1 + the minimum of the two jumps. The two jumps are jump(i + 1) and jump(i + 2).
        return 1 + min(jump(i + 1), jump(i + 2))

    # Here we are calling the jump function with the index 0.
    # eg: c = [0, 0, 1, 0, 0, 1, 0]
    # jump(0) = 1 + min(jump(1), jump(2))
    return jump(0)


# Solution: 3 - Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(n)
def jumpingOnClouds(c):
    dp = [0] + [float("inf")] * (len(c) - 1)

    for i in range(len(c)):
        if c[i] == 1:
            continue

        for j in range(i + 1, min(i + 3, len(c))):
            dp[j] = min(dp[j], dp[i] + 1)

    return dp[-1]


# Input

c = [0, 0, 1, 0, 0, 1, 0]
print(jumpingOnClouds(c))
