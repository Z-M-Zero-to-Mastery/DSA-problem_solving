# An English text needs to be encrypted using the following encryption scheme.
# First, the spaces are removed from the text. Let l be the length of this text.
# Then, characters are written into a grid, whose rows and columns have the following constraints:

# ⌊l‾‾√⌋≤rows≤column≤⌈l‾‾√⌉, where ⌊x⌋ is floor function and ⌈x⌉ is ceil function

# Example:
# s = if man was meant to stay on the ground god would have given us roots
# After removing spaces, the string is 54 characters long. sqrt(54) is between 7 and 8, so it is written in the form of a grid with 7 rows and 8 columns.

# ifmanwas
# meanttos
# tayonthe
# groundgo
# dwouldha
# vegivenu
# sroots

# Ensure that rows×columns≥L
# If multiple grids satisfy the above conditions, choose the one with the minimum area, i.e. rows×columns.

# The encoded message is obtained by displaying the characters of each column, with a space between column texts. The encoded message for the grid above is:

# imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau
# You will be given a message in English with no spaces between the words. The maximum message length can be characters. Print the encoded message.

# Here are some more examples:

# Sample Input:
# haveaniceday

# Sample Output:
# hae and via ecy

# Explanation:
# L=12,  sqrt(12) is between 3 and 4.
# Rewritten with 3 rows and 4 columns:
# have
# anic
# eday

# Sample Input: 2
# feedthedog

# Sample Output: 2
# fto ehg ee dd

# Explanation:
# L=10, sqrt(10) is between 3 and 4.
# Rewritten with 3 rows and 4 columns:
# feed
# thed
# og

# Sample Input: 3
# chillout

# Sample Output: 3
# clu hlt io

# Explanation:
# L=8, sqrt(8) is between 2 and 3.
# Rewritten with 3 columns and 3 rows (2*3=6<8 so we have to use 3x3)
# chi
# llo
# ut

# Solution: 1
import math


def encryption(s):
    # Remove spaces e.g. "have a nice day" -> "haveaniceday"
    s = s.replace(" ", "")
    l = len(s)
    row = math.floor(math.sqrt(l))
    col = math.ceil(math.sqrt(l))

    # If row*col < l, then row = col
    if row * col < l:
        row = col

    # Create a grid with row and col
    # e.g. "haveaniceday" -> "have anic eday"
    result = ""

    # Loop through the grid and add space after each column
    # first loop through the column, then loop through the row
    for i in range(col):
        for j in range(row):
            # Check if i+j*col < l to avoid index out of range error
            # e.g. i = 3, j = 1, col = 4, row = 3, l = 12 -> 3+1*4 = 7 < 12
            if i + j * col < l:
                # Add each character to the result string
                # e.g. i = 3, j = 1, col = 4, row = 3, l = 12 -> 3+1*4 = 7 -> s[7] = "e"
                result += s[i + j * col]

        # This is to add space after each column
        # e.g. "have anic eday" -> "have anic eday "
        result += " "

    return result


# Solution: 2 Using list
import math


def encryption(s):
    l = math.sqrt(len(s))
    row = math.floor(l)
    col = math.ceil(l)
    ar = []

    # Loop through the grid and add space after each column
    for i in range(col):
        # temp is a list to store each column
        temp = []
        # j is the index of each column
        j = 0

        # Loop through the row and add each character to the temp list
        # i + j < len(s) to avoid index out of range error
        while i + j < len(s):
            # Add each character to the temp list
            # eg: i = 3, j = 1, s[ 3 + 4] = s[7] = "e"
            temp.append(s[i + j])
            j += col

        # Add each column to the ar list and join them with space
        # eg: temp = ["h", "a", "v", "e"], ar = ["have"]
        ar.append("".join(temp))

    # Join each column with space and return the result string
    # eg: ar = ["have", "anic", "eday"], return "have anic eday"
    return " ".join(ar)


# Input
s = "have a nice day"
print(encryption(s))
