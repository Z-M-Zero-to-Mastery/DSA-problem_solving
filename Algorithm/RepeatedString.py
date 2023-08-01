# There is a string, s, of lowercase English letters that is repeated infinitely many times. Given an integer, n, find and print the number of letter a's in the first n letters of the infinite string.
# Example: s = 'abcac' n = 10
# The substring we consider is abcacabcac, the first 10 characters of the infinite string. There are 4 occurrences of a in the substring.
# Returns : int: the frequency of a in the substring

# Sample Input 0
# aba
# 10
# Sample Output 0
# 7
# Explanation 0
# The first n=10 letters of the infinite string are abaabaabaa. Because there are 7 a's, we return 7.

# Sample Input 1
# a
# 1000000000000
# Sample Output 1
# 1000000000000
# Explanation 1
# Because all of the first n=1000000000000 letters of the infinite string are a, we return 1000000000000.


# Solution: 1 - Brute Force
def repeatedString(s, n):
    count = 0

    # Count the number of a's in the string
    # eg: s = 'abcac' , n = 10
    for i in range(n):
        # Here i % len(s) will give the index of the string
        # eg: i = 0, 0 % 5 = 0, s[0] = 'a'
        # eg: i = 1, 1 % 5 = 1, s[1] = 'b'
        # eg: i = 2, 2 % 5 = 2, s[2] = 'c'
        # eg: i = 3, 3 % 5 = 3, s[3] = 'a'
        # eg: i = 4, 4 % 5 = 4, s[4] = 'c'
        # eg: i = 5, 5 % 5 = 0, s[0] = 'a'
        # eg: i = 6, 6 % 5 = 1, s[1] = 'b'
        # eg: i = 7, 7 % 5 = 2, s[2] = 'c'
        # .....
        if s[i % len(s)] == "a":
            count += 1

    return count


# Solution: 2 - Optimized
def repeatedString(s, n):
    count = 0

    # Count the number of a's in the string
    # eg: s = 'abcac' , n = 10 , count becomes 2
    for i in range(len(s)):
        if s[i] == "a":
            count += 1

    # Here we are dividing n by the length of the string to get the number of times the string is repeated
    # eg: n = 10, len(s) = 5, n // len(s) = 2
    # count = 2 * 2 = 4
    count *= n // len(s)

    # Here we are getting the remainder of the string and checking if the character is 'a'
    # eg: n = 10, len(s) = 5, n % len(s) = 0
    # eg: s = 'aba' , n = 10, len(s) = 3, n % len(s) = 1
    for i in range(n % len(s)):
        if s[i] == "a":
            count += 1

    return count


# Input
s = "abcac"
n = 10

print(repeatedString(s, n))
