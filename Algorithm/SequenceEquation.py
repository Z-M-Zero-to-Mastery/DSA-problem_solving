# Given a sequence of n integers, p(1), p(2), ...p(n) where each element is distinct and satisfies 1 <= p(x) <= n. For each x where 1 <= x <=n, that is x increments from 1 to n, find any integer y such that p(p(y)) = x and keep a history of the values of y in a return array.
# Example
# p = [5, 2, 1, 3, 4]
# Each value of x between 1 and 5, the length of the array, is analyzed as follows:
# x = 1 = p[3], p[4] = 3, so p[p[4]] = 1
# x = 2 = p[2], p[2] = 2, so p[p[2]] = 2
# x = 3 = p[4], p[5] = 4, so p[p[5]] = 3
# x = 4 = p[5], p[1] = 5, so p[p[1]] = 4
# x = 5 = p[1], p[3] = 1, so p[p[3]] = 5
# The values for y are [4, 2, 5, 1, 3].

# Return an integer array containing the values of y in order.

# Sample Input 0
# 3
# 2 3 1

# Sample Output 0
# 2
# 3
# 1

# Explanation 0
# Given the values of p(1) = 2, p(2) = 3, and p(3) = 1, we calculate and print the following values for each x from 1 to n:
# x = 1 = p[3] = 1, so p[p[3]] = p[1] = 2
# x = 2 = p[1] = 2, so p[p[1]] = p[2] = 3
# x = 3 = p[2] = 3, so p[p[2]] = p[3] = 1

# Sample Input 1
# 5
# 4 3 5 1 2

# Sample Output 1
# 1
# 3
# 5
# 4
# 2

# Explanation 1
# Given the values of p(1) = 4, p(2) = 3, p(3) = 5, p(4) = 1, and p(5) = 2, we calculate and print the following values for each x from 1 to n:
# x = 1 = p[4] = 1, so p[p[4]] = p[1] = 4
# x = 2 = p[2] = 3, so p[p[2]] = p[3] = 5
# x = 3 = p[5] = 2, so p[p[5]] = p[2] = 3
# x = 4 = p[1] = 4, so p[p[1]] = p[4] = 1
# x = 5 = p[3] = 5, so p[p[3]] = p[5] = 2


# Solution 1
def permutationEquation(p):
    # Write your code here
    result = []

    # It will iterate from 1 to len(p)+1
    for i in range(1, len(p) + 1):
        # It will append the index of the index of i+1 in p
        # p.index(i) will return the index of i in p
        # p.index(p.index(i)+1) will return the index of i+1 in p and p.index(p.index(i)+1)+1 will return the index of i+1 in p and add 1 to it
        # eg:
        # p = [5, 2, 1, 3, 4]
        # i = 1
        # p.index(p.index(i)+1) = p.index(p.index(1)+1) = p.index(2+1) = p.index(3 +1) = p.index(4) = 4
        result.append(p.index(p.index(i) + 1) + 1)

    return result


# Solution 2 (Using Dictionary)
def permutationEquation(p):
    d = {}

    # It will create a dictionary with key as the value of p and value as the index of p
    for i in range(len(p)):
        # p[i] will return the value of p at index i
        d[p[i]] = i + 1

    # eg: p = [5, 2, 1, 3, 4]
    # d = {5: 1, 2: 2, 1: 3, 3: 4, 4: 5}

    result = []

    # It will iterate from 1 to len(p)+1
    for i in range(1, len(p) + 1):
        # It will append the value of the value of i in d
        # eg: i = 1 and d[i] = d[1] = 3 and d[d[i]] = d[d[1]] = d[3] = 4 and d[d[i]] = d[d[3]] = d[4] = 5 and d[d[i]] = d[d[4]] = d[5] = 1 and continue the loop
        result.append(d[d[i]])

    return result


# Solution 3 (Using List Comprehension)
def permutationEquation(p):
    return [p.index(p.index(i) + 1) + 1 for i in range(1, len(p) + 1)]
