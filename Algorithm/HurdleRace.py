# A video player plays a game in which the character competes in a hurdle race. Hurdles are of varying heights, and the characters have a maximum height they can jump. There is a magic potion they can take that will increase their maximum jump height by 1 unit for each dose. How many doses of the potion must the character take to be able to jump all of the hurdles. If the character can already clear all of the hurdles, return 0.
# Example
# height = [1,2,3,3,2]
# k = 1
# The character can jump 1 unit high initially and must take 3-1=2 doses of potion to be able to jump all of the hurdles.
# Returns 2

# Sample Input 0
# 5 4
# 1 6 3 5 2

# Sample Output 0
# 2

# Explanation 0
# Dan's character can jump a maximum of k=4 units, but the tallest hurdle has a height of h1=6: To be able to jump all the hurdles, Dan must drink 6-4=2 doses.

# Sample Input 1
# 5 7
# 2 5 4 5 2

# Sample Output 1
# 0

# Explanation 1
# The character can already jump 7 units high, so return 0.


# Solution: 1
def hurdleRace(k, height):
    if max(height) > k:
        return max(height) - k
    else:
        return 0


# Solution: 2
def hurdleRace(k, height):
    return max(height) - k if max(height) > k else 0


# Input
k = 4
height = [1, 6, 3, 5, 2]
print(hurdleRace(k, height))
