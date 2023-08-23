# Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.

# Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:

# It must be greater than the original word
# It must be the smallest word that meets the first condition
# For example,
# w = 'abcd'
# The next largest word is 'abdc'

# complete the function biggerIsGreater below to create and return the new string meeting the criteria. If it is not possible, return no answer.
# Return the new string meeting the criteria, or no answer if not possible.

# Sample Input 0
# 5
# ab
# bb
# hefg
# dhck
# dkhc

# Sample Output 0
# ba
# no answer
# hegf
# dhkc
# hcdk

# Explanation 0
# Test case 1:
# ba is the only string which can be made by rearranging ab. It is greater.
# Test case 2:
# It is not possible to rearrange bb and get a greater string.
# Test case 3:
# hegf is the next string greater than hefg.
# Test case 4:
# dhkc is the next string greater than dhck.
# Test case 5:
# hcdk is the next string greater than dkhc.

# Sample Input 1
# 6
# lmno
# dcba
# dcbb
# abdc
# abcd
# fedcbabcd

# Sample Output 1
# lmon
# no answer
# no answer
# acbd
# abdc
# fedcbabdc

# Explanation 1
# Test case 1:
# lmon is the next largest string after lmno.
# Test case 2:
# There exists no string whose lexicographic order is greater than dcba and smaller than dcbb.
# Test case 3:
# There exists no string whose lexicographic order is greater than dcbb and smaller than abdc.
# Test case 4:
# abdc is the next largest string after abcd.
# Test case 5:
# abdc is the next largest string after abcd.
# Test case 6:
# fedcbabdc is the next largest string after fedcbabcd.


# Solution 1 Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(n)


def biggerIsGreater(w):
    # Write your code here
    # Brute Force
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    # w = list(w)
    # for i in range(len(w)-1, -1, -1):
    #     for j in range(i-1, -1, -1):
    #         if w[i] > w[j]:
    #             w[i], w[j] = w[j], w[i]
    #             return ''.join(w)
    # return 'no answer'

    # Optimized
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    # w is list of characters in string w eg. w = 'abcd' => w = ['a', 'b', 'c', 'd'] and i = len(w)-1 , i = 3
    w = list(w)
    i = len(w) - 1

    # This while loop will find the first character from the end which is smaller than its next character
    # eg. w = ['a', 'b', 'c', 'd'] => i = 3, w[3] = 'd' and w[3-1] = 'c' => w[3] > w[3-1] => True => i = 2
    while i > 0 and w[i - 1] >= w[i]:
        # If above condition is not true then we will decrement i by 1 and check again
        # i is decerementing because we want to find the first character from the end which is smaller than its next character
        i -= 1

    # If i is 0 then it means that the string is in descending order and there is no next greater string
    if i <= 0:
        return "no answer"

    # Now we will find the character which is just greater than the character at index i-1
    j = len(w) - 1

    # This loop is to find the character which is just greater than the character at index i-1
    # eg. w = ['a', 'b', 'c', 'd'] => i = 2, w[2] = 'c' and w[3] = 'd' => w[2] < w[3] => True => j = 3
    while w[j] <= w[i - 1]:
        j -= 1

    # Now we will swap the characters at index i-1 and j
    # eg. w = ['a', 'b', 'c', 'd'] => i = 2, j = 3 => w[i-1] = 'c' and w[j] = 'd' => w[i-1], w[j] = w[j], w[i-1] => w = ['a', 'b', 'd', 'c']
    w[i - 1], w[j] = w[j], w[i - 1]
    # Now we will reverse the string from index i to the end of the string, because we want the smallest string which is greater than the original string
    # eg : w = ['a', 'b', 'd', 'c'] => i = 2 => w[i:] = ['d', 'c'] => w[len(w)-1:i-1:-1] = ['c', 'd'] => w[i:] = ['c', 'd']
    w[i:] = w[len(w) - 1 : i - 1 : -1]

    # Now we will return the string by joining the characters in the list w
    # eg. w = ['a', 'b', 'd', 'c'] => ''.join(w) => 'abdc'
    return "".join(w)


# Input

w = "abcd"

print(biggerIsGreater(w))
