# A child is playing a cloud hopping game. In this game, there are sequentially numbered clouds that can be thunderheads or cumulus clouds. The character must jump from cloud to cloud until it reaches the start again.
# There is an array of clouds, c and an energy level e=100. The character starts from c[0] and uses 1 unit of energy to make a jump of size k to cloud c[(i+k)%n]. If it lands on a thundercloud, c[i]=1, its energy (e) decreases by 2 additional units. The game ends when the character lands back on cloud 0. Given the values of n, k, and the configuration of the clouds as an array c, determine the final value of e after the game ends.
# Example:
# c = [0,0,1,0] k = 2
# The indices of the path are 0 -> 2 -> 0. The energy level reduces by 1 for each jump to 98. The character landed on one thunderhead at an additional cost of 2 energy units. The final energy level is 96.
# Note: Recall that % refers to the modulo operation. In this case, it serves to make the route circular. If the character is at c[n-1] and jumps 1, it will arrive at c[0].

# Returns the final energy level

# Sample Input:
# 8 2
# 0 0 1 0 0 1 1 0  # c = [0,0,1,0,0,1,1,0] k = 2

# Sample Output:
# 92

# Explanation:
# In the diagram below, red clouds are thunderheads and purple clouds are cumulus clouds:
# Game Board Diagram
# Observe that our thunderheads are the clouds numbered 2, 5, and 6. The character makes the following sequence of moves: 0 -> 2 -> 4 -> 6 -> 0 -> 2 -> 4 -> 6 -> 0. The arrows show the direction of travel and the cumulative cost of each jump.


# Solution: 1
def jumpingOnClouds(c, k):
    n = len(c)
    e = 100
    i = 0

    while True:
        # This is the first jump and it is not a thunderhead cloud so we don't need to subtract 2 from energy
        # eg: c = [0,0,1,0] k = 2 => e = 100 - 1 - 2 * 0 = 99
        # in second jump i = 2 and k = 2 so (i + k) % n = (2 + 2) % 4 = 0 (This is the starting point)
        e = e - 1 - 2 * c[i]
        # In first jump i = 0 and k = 2 so (i + k) % n = (0 + 2) % 4 = 2
        # In second jump i = 2 and k = 2 so (i + k) % n = (2 + 2) % 4 = 0 (This is the starting point)
        i = (i + k) % n

        if i == 0:
            return e


# Solution: 2 (Using for loop)
def jumpingOnClouds(c, k):
    n = len(c)
    e = 100
    i = 0

    for i in range(0, n, k):
        e = e - 1 - 2 * c[i]

    return e
