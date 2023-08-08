# You will be given a square chess board with one queen and a number of obstacles placed on it. Determine how many squares the queen can attack.
# A queen is standing on an n x n chessboard. The chess board's rows are numbered from 1 to n, going from bottom to top. Its columns are numbered from 1 to n, going from left to right. Each square is referenced by a tuple, (r, c), describing the row, r, and column, c, where the square is located. The queen is standing at position (rq, cq). In a single move, she can attack any square in any of the eight directions (left, right, up, down, and the four diagonals). In the diagram below, the green circles denote all the cells the queen can attack from (4, 4):

# _|_|_|_|_|_|_|_
# _|_|_|_|_|_|_|_
# _|_|_|_|_|_|_|_
# _|_|_|Q|_|_|_|_
# _|_|_|_|_|_|_|_
# _|_|_|_|_|_|_|_
# _|_|_|_|_|_|_|_
# _|_|_|_|_|_|_|_


# There are obstacles on the chessboard, each preventing the queen from attacking any square beyond it on that path. For example, an obstacle at location (3, 5) in the diagram above prevents the queen from attacking cells (3, 5), (2, 6), and (1, 7):

# _|_|_|_|_|_|_|_
# _|_|_|_|_|_|_|_
# _|_|_|_|_|_|_|_
# _|_|_|Q|_|_|_|_
# _|_|_|_|x|_|_|_
# _|_|_|_|_|_|_|_
# _|_|_|_|_|_|_|_
# _|_|_|_|_|_|_|_


# Given the queen's position and the locations of all the obstacles, find and print the number of squares the queen can attack from her position at (rq, cq). In the board above, there are 24 such squares.

# Function Description
# Complete the queensAttack function in the editor below. It should return an integer that describes the number of squares the queen can attack.
# queensAttack has the following parameters:
# n: an integer, the number of rows and columns in the board
# k: an integer, the number of obstacles on the board
# r_q: integer, the row number of the queen's position
# c_q: integer, the column number of the queen's position
# obstacles: a two dimensional array of integers where each element is an array of 2 integers, the row and column of an obstacle

# Returns : an integer that denotes the number of squares the queen can attack

# Sample Input 0
# 4 0
# 4 4

# Sample Output 0
# 9

# Explanation 0
# The queen is standing at position (4, 4) on a 4 x 4 chessboard with no obstacles:

# 1 _|_|_|_|_
# 2 _|_|_|_|_
# 3 _|_|_|_|_
# 4 _|_|_|Q|_
#   1 2 3 4

# Sample Input 1
# 5 3
# 4 3
# 5 5
# 4 2
# 2 3

# Sample Output 1
# 10

# Explanation 1
# The queen is standing at position (4, 3) on a 5 x 5 chessboard with k = 3 obstacles:

# 1 _|_|_|_|_
# 2 _|_|_|_|_
# 3 _|_|_|_|_
# 4 _|_|Q|_|_
# 5 _|_|_|_|_
#  1  2 3 4 5

# The number of squares she can attack from that position is 10.


# Solution 1 - Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
def queensAttack(n, k, r_q, c_q, obstacles):
    # Create a board
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Place the queen on the board
    board[r_q - 1][c_q - 1] = 1

    # Place the obstacles on the board
    for obstacle in obstacles:
        board[obstacle[0] - 1][obstacle[1] - 1] = -1

    # Count the number of squares the queen can attack
    count = 0
    # Check the left side of the queen
    for i in range(c_q - 2, -1, -1):
        if board[r_q - 1][i] == -1:
            break
        else:
            count += 1
    # Check the right side of the queen
    for i in range(c_q, n):
        if board[r_q - 1][i] == -1:
            break
        else:
            count += 1
    # Check the top side of the queen
    for i in range(r_q - 2, -1, -1):
        if board[i][c_q - 1] == -1:
            break
        else:
            count += 1
    # Check the bottom side of the queen
    for i in range(r_q, n):
        if board[i][c_q - 1] == -1:
            break
        else:
            count += 1
    # Check the top left diagonal of the queen
    i, j = r_q - 2, c_q - 2
    while i >= 0 and j >= 0:
        if board[i][j] == -1:
            break
        else:
            count += 1
        i -= 1
        j -= 1
    # Check the top right diagonal of the queen
    i, j = r_q - 2, c_q
    while i >= 0 and j < n:
        if board[i][j] == -1:
            break
        else:
            count += 1
        i -= 1
        j += 1
    # Check the bottom left diagonal of the queen
    i, j = r_q, c_q - 2
    while i < n and j >= 0:
        if board[i][j] == -1:
            break
        else:
            count += 1

        i += 1
        j -= 1
    # Check the bottom right diagonal of the queen
    i, j = r_q, c_q
    while i < n and j < n:
        if board[i][j] == -1:
            break
        else:
            count += 1
        i += 1
        j += 1

    return count


# Solution 2 - Optimized
# Time Complexity: O(k)
# Space Complexity: O(1)
def queensAttack(n, k, r_q, c_q, obstacles):
    count = 0
    # Create a set of obstacles
    # This will allow us to check if an obstacle is in the set in constant time O(1)
    # instead of checking if an obstacle is in the list in linear time O(k)
    # Eg : obstacles = [(1, 1), (2, 2), (3, 3)] -> set([(1, 1), (2, 2), (3, 3)])
    # obstacles = [(5, 5), (4, 2), (2, 3)] -> set([(5, 5), (4, 2), (2, 3)])
    obstacles = set([(obstacle[0], obstacle[1]) for obstacle in obstacles])

    # Check the left side of the queen
    # Eg : n = 5, r_q = 4, c_q = 3, obstacles = [(5, 5), (4, 2), (2, 3)]
    # i , j = 4, 2
    i, j = r_q, c_q - 1
    while j >= 1:
        if (i, j) in obstacles:
            break
        else:
            count += 1
        j -= 1
    # Check the right side of the queen
    i, j = r_q, c_q + 1
    while j <= n:
        if (i, j) in obstacles:
            break
        else:
            count += 1
        j += 1
    # Check the top side of the queen
    i, j = r_q - 1, c_q
    while i >= 1:
        if (i, j) in obstacles:
            break
        else:
            count += 1
        i -= 1
    # Check the bottom side of the queen
    i, j = r_q + 1, c_q
    while i <= n:
        if (i, j) in obstacles:
            break
        else:
            count += 1
        i += 1
    # Check the top left diagonal of the queen
    i, j = r_q - 1, c_q - 1
    while i >= 1 and j >= 1:
        if (i, j) in obstacles:
            break
        else:
            count += 1
        i -= 1
        j -= 1
    # Check the top right diagonal of the queen
    i, j = r_q - 1, c_q + 1
    while i >= 1 and j <= n:
        if (i, j) in obstacles:
            break
        else:
            count += 1
        i -= 1
        j += 1
    # Check the bottom left diagonal of the queen
    i, j = r_q + 1, c_q - 1
    while i <= n and j >= 1:
        if (i, j) in obstacles:
            break
        else:
            count += 1
        i += 1
        j -= 1
    # Check the bottom right diagonal of the queen
    i, j = r_q + 1, c_q + 1
    while i <= n and j <= n:
        if (i, j) in obstacles:
            break
        else:
            count += 1
        i += 1
        j += 1

    return count


# Solution 3 - Optimized (Using dictionary)
# Time Complexity: O(k)
# Space Complexity: O(1)
def queensAttack(n, k, r_q, c_q, obstacles):
    total = 0
    # Create a dictionary of obstacles
    obs = {}

    # Eg : obstacles = [(1, 1), (2, 2), (3, 3)] -> obs = {1: {1: 1}, 2: {2: 1}, 3: {3: 1}}
    # obstacles = [(5, 5), (4, 2), (2, 3)] -> obs = {5: {5: 1}, 4: {2: 1}, 2: {3: 1}}
    for i, j in obstacles:
        if i in obs:
            obs[i][j] = 1
        else:
            obs[i] = {j: 1}

    # Check if the position is within the board
    def limit(x, y):
        # Eg : n = 5, r_q = 4, c_q = 3 -> True
        # n = 5, r_q = 6, c_q = 3 -> False
        return True if 1 <= x <= n and 1 <= y <= n else False

    # Check the number of squares the queen can attack in a particular direction
    # parameters : x, y -> position of the queen on the board , xi, yi -> direction
    def check(x, y, xi, yi):
        # Eg : x = 4, y = 3, xi = 0, yi = 1 -> count = 1
        count = 0
        x += xi
        y += yi
        # Eg : x = 4, y = 4 -> True and obs.get(4, {}).get(4, 0) = 0 -> True
        while limit(x, y) and obs.get(x, {}).get(y, 0) == 0:
            count += 1
            x += xi
            y += yi

            return count

    # Check the number of squares the queen can attack in all directions
    r = [0, 0, 1, -1, 1, -1, 1, -1]
    c = [1, -1, 0, 0, 1, -1, -1, 1]

    # This is looping through the list of directions
    for i, j in zip(r, c):
        # Calling the check function to check the number of squares the queen can attack in a particular direction
        # Eg : r_q = 4, c_q = 3, i = 0, j = 1 -> total = 1
        # r_q = 4, c_q = 3, i = 0, j = -1 -> total = 2
        # r_q = 4, c_q = 3, i = 1, j = 0 -> total = 3
        # r_q = 4, c_q = 3, i = -1, j = 0 -> total = 4
        # .......
        # .......
        total += check(r_q, c_q, i, j)

    return total


# Input
n = 5
k = 3
r_q = 4
c_q = 3
obstacles = [(5, 5), (4, 2), (2, 3)]

result = queensAttack(n, k, r_q, c_q, obstacles)
print(result)
