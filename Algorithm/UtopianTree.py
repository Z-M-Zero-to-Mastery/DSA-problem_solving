# The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

# A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after n growth cycles?

# For example, if the number of growth cycles is n = 5, the calculations are as follows:

# Period  Height
# 0          1
# 1          2
# 2          3
# 3          6
# 4          7
# 5          14

# Return the height of the tree after the given number of cycles.

# Sample Input
# 3
# 0
# 1
# 4

# Sample Output
# 1
# 2
# 7

# Explanation
# There are 3 test cases.

# In the first case (n = 0), the initial height (h = 1) of the tree remains unchanged. In the second case (n = 1), the tree doubles in height and is 2 meters tall after the spring cycle. In the third case (n = 4), the tree doubles its height in spring (n = 1, h = 2), then grows a meter in summer (n = 2, h = 3), then doubles after the next spring (n = 3, h = 6), and grows another meter after summer (n = 4, h = 7). Thus, at the end of 4 cycles, its height is 7 meters.

# Solution


def utopianTree(n):
    height = 1

    for i in range(n):
        if i % 2 == 0:
            height *= 2
        else:
            height += 1

    return height


# Input

n = 3
print(utopianTree(n))
