# David has several containers, each with a number of balls in it. He has just enough containers to sort each type of ball he has into its own container. David wants to sort the balls using his sort method.

# David wants to perform some number of swap operations such that:

# Each container contains only balls of the same type.
# No two balls of the same type are located in different containers.

# You must perform  queries where each query is in the form of a matrix, . For each query, print Possible on a new line if David can satisfy the conditions above for the given matrix. Otherwise, print Impossible.

# Example
# container = [[1, 4], [2, 3]]
# David has n = 2 containers and 2 different types of balls, both of which are numbered from 0 to n-1 = 1. The distribution of ball types per container are shown in the following diagram.

#   0   1
# 0 [1, 4]
# 1 [2, 3]

# container 0 contains 1 ball of type 0 and 4 balls of type 1.
# _ _ _ _ _ _ _ _
# | (0) (1) (1) |
# |   (1)  (1)  |

# container 1 contains 2 balls of type 0 and 3 balls of type 1.
# _ _ _ _ _ _ _ _
# | (0) (0) (1) |
# |   (1)  (1)  |

# In the first query, there are two possible permutations:

# 1. Swap the balls in both containers such that container  contains two balls of type 1 and container  contains two balls of type 0.
# 2. Swap the balls in both containers such that container  contains one ball of type 0 and container  contains three balls of type 1.

# In the second query, there is no way to arrange the containers such that each container contains balls of the same type.

# In this case, there is no way to have all green balls in one container and all red in the other using only swap operations. Return Impossible.

# You must perform q queries where each query is in the form of a matrix, M. For each query, print Possible on a new line if David can satisfy the conditions above for the given matrix. Otherwise, print Impossible

# Sample Input 0
# 2
# 2
# 1 1
# 1 1
# 2
# 0 2
# 1 1

# Sample Output 0
# Possible
# Impossible

# Explanation 0
# We perform the following q = 2 queries:

# 1. The diagram below depicts one possible way to satisfy David's requirements for the first query:

#   0   1
# 0 [1, 1]
# 1 [1, 1]

# Thus, we print Possible on a new line.
# 2. The diagram below depicts the matrix for the second query:

#   0   1
# 0 [0, 2]
# 1 [1, 1]

# No matter how many times we swap balls of type 0 and type 1 between the two containers, we'll never end up with one container only containing type 0 and the other container only containing type 1. Thus, we print Impossible on a new line.

# Sample Input 1
# 2
# 3
# 1 3 1
# 2 1 2
# 3 3 3
# 3
# 0 2 1
# 1 1 1
# 2 0 0

# Sample Output 1
# Impossible
# Possible

# Explanation 1
# We perform the following q = 2 queries:

# 1. The following matrix depicts one possible way to satisfy David's requirements for the first query:

#   0   1   2
# 0 [1, 3, 1]
# 1 [2, 1, 2]
# 2 [3, 3, 3]

# No matter how many times we swap balls of type 0 and type 1 between the two containers, we'll never end up with one container only containing type 0 and the other container only containing type 1. Thus, we print Impossible on a new line.

# 2. The following matrix depicts one possible way to satisfy David's requirements for the second query:

#   0   1   2
# 0 [0, 2, 1]
# 1 [1, 1, 1]
# 2 [2, 0, 0]

# Thus, we print Possible on a new line.


# Solution 1 - Brute Force
def organizingContainers(container):
    #     # Write your code here
    #     # Brute Force
    #     # Time Complexity: O(n^2)
    #     # Space Complexity: O(n)
    # Take the first container and check if it can be emptied by moving balls to other containers
    n = len(container)
    # Create a list of balls in each container and a list of containers with balls of each type
    balls = [0] * n
    containers = [0] * n

    # Loop through the containers and balls
    for i in range(n):
        for j in range(n):
            # Add the balls in each container and the containers with balls of each type
            # The first container will be the balls and the second will be the containers with balls of each type
            # eg: container = [[1, 4], [2, 3]]
            # balls = [5, 5] and containers = [3, 7]
            # balls[0] += container[0][0] = 1 and balls[1] += container[0][1] = 4
            # containers[0] += container[0][0] = 1 and containers[1] += container[1][0] = 2
            # balls[0] += container[1][0] = 2 and balls[1] += container[1][1] = 3
            # containers[0] += container[0][1] = 4 and containers[1] += container[1][1] = 3
            balls[i] += container[i][j]
            containers[i] += container[j][i]

    # Sort the balls and containers, so that we can compare them
    balls.sort()
    containers.sort()

    # Check if the balls and containers are equal , If they are equal then we can empty the first container by moving balls to other containers
    if balls == containers:
        return "Possible"
    else:
        return "Impossible"


# Input

container = [[1, 4], [2, 3]]

print(organizingContainers(container))
