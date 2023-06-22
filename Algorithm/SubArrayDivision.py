# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

# Lily decides to share a contiguous segment of the bar selected such that:

# The length of the segment matches Ron's birth month, and,
# The sum of the integers on the squares is equal to his birth day.
# Determine how many ways she can divide the chocolate.

# Example
# s = [2,2,1,3,2]
# d = 4
# m = 2

# Constraints
# Lily wants to find segments summing to Ron's birth day, d = 4 with a length equalling his birth month, m = 2.
# In this case, there are two segments meeting her criteria: [2,2] and [1,3].

# Sample Input 0
# 5
# 1 2 1 3 2
# 3 2

# Sample Output 0
# 2

# Explanation 0
# Lily wants to give Ron m = 2 squares summing to d = 3.


# Solution 1:
def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        if sum(s[i : i + m]) == d:
            count += 1
    return count


# Solution 2:
def birthday(s, d, m):
    count = 0

    # Loop through the list
    for i in range(len(s)):
        # Get the size of the subarray
        size = len(s[i : m + i])

        # Check if the size of the subarray is equal to m
        if size == m:
            # Get the sum of the subarray
            total = sum(s[i : m + i])
            # Check if the sum of the subarray is equal to d
            if total == d:
                count += 1

    return count


# Solution 3:
def birthday(s, d, m):
    count = 0
    total = sum(s[:m])

    if total == d:
        count += 1

    for i in range(m, len(s)):
        total += s[i]
        total -= s[i - m]
        if total == d:
            count += 1

    return count


# Input

s = [1, 2, 1, 3, 2]
d = 3
m = 2
print(birthday(s, d, m))  # 2
