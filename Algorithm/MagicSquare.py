# We define a magic square to be an n * n matrix of distinct positive integers from 1 to n2 where the sum of any row, column, or diagonal of length n is always equal to the same number: the magic constant.

# You will be given a 3*3 matrix s of integers in the inclusive range [1, 9]. We can convert any digit a to any other digit b in the range  at cost of |a-b|. Given s, convert it into a magic square at minimal cost. Print this cost on a new line.

# Note: The resulting magic square must contain distinct integers in the inclusive range [1, 9].

# For example, we start with the following matrix s:

# 5 3 4
# 1 5 8
# 6 4 2
# We can convert it to the following magic square:

# 8 3 4
# 1 5 9
# 6 7 2
# This took three replacements at a cost of |5-8| + |8-9| + |4-7| = 7.

# Return the minimal cost of converting a 3*3 matrix into a magic square.

# Sample Input 0

# 4 9 2
# 3 5 7
# 8 1 5
# Sample Output 0

# 1
# Explanation 0

# If we change the bottom right value, s[2][2], from 5 to 6 at a cost of |6-5| = 1, s becomes a magic square at the minimum possible cost.

# Sample Input 1

# 4 8 2
# 4 5 7
# 6 1 6
# Sample Output 1

# 4
# Explanation 1

# Using 0-based indexing, if we make

# s[0][1]->9 at a cost of |9-8| = 1
# s[1][0]->3 at a cost of |3-4| = 1
# s[2][0]->8 at a cost of |8-6| = 2,
# then the total cost will be 1+1+2=4.

#  REFERENCES: https://mindyourdecisions.com/blog/2015/11/08/how-many-3x3-magic-squares-are-there-sunday-puzzle/


# Solution 1:
# 1. Create a list of all possible magic squares
# 2. Compare the input matrix with each magic square and find the minimum cost
def compare_lists(list1, list2):
    sum_of_differences = 0
    for i in range(len(list1)):
        sum_of_differences += abs(list1[i] - list2[i])
    return sum_of_differences


def formingMagicSquare(s):
    # Write your code here

    l1 = [6, 1, 8, 7, 5, 3, 2, 9, 4]
    l2 = [8, 1, 6, 3, 5, 7, 4, 9, 2]
    l3 = [6, 7, 2, 1, 5, 9, 8, 3, 4]
    l4 = [8, 3, 4, 1, 5, 9, 6, 7, 2]
    l5 = [2, 7, 6, 9, 5, 1, 4, 3, 8]
    l6 = [4, 3, 8, 9, 5, 1, 2, 7, 6]
    l7 = [2, 9, 4, 7, 5, 3, 6, 1, 8]
    l8 = [4, 9, 2, 3, 5, 7, 8, 1, 6]

    td = []
    lf = []

    for i in s:
        for j in i:
            lf.append(j)

    for i in [l1, l2, l3, l4, l5, l6, l7, l8]:
        td.append(compare_lists(i, lf))

    return min(td)


# Input
s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
print(formingMagicSquare(s))
