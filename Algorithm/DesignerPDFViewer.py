# When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently. For example:

# In this challenge, you will be given a list of letter heights in the alphabet and a string. Using the letter heights given, determine the area of the rectangle highlight in assuming all letters are wide.
# There is an list of 26 character heights aligned by index to their letters. For example, 'a' is at index 0 and 'z' is at index 25. There will also be a string. Using the letter heights given, determine the area of the rectangle highlight in assuming all letters are wide.

# Example
# h=[1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5]
# word='torn'
# The heights are t=2, o=1, r=1 and n=1. The tallest letter is 2 high and there are 4 letters. The hightlighted area will be 2*4=8 so the answer is 8.

# Sample Input 0
# 1 3 1 3 1 4 1 3 2 5 5 5 5 1 1 5 5 1 5 2 5 5 5 5 5 5
# abc

# Sample Output 0
# 9

# Explanation 0
# We are highlighting the word abc:
# Letter heights are a=1, b=3 and c=1. The tallest letter, b, is 3 high. The selection area for this word is 3*1=3.

# Sample Input 1
# 1 3 1 3 1 4 1 3 2 5 5 5 5 1 1 5 5 1 5 2 5 5 5 5 5 5 7
# zaba

# Sample Output 1
# 28

# Explanation 1
# The tallest letters are 5 high and there are 4 letters. The hightlighted area will be 7*4=28.


# Solution 1
def designerPdfViewer(h, word):
    height = 0

    for i in word:
        # ord() returns an integer representing the Unicode character
        height = max(height, h[ord(i) - ord("a")])

    return height * len(word)


# Solution 2
def designerPdfViewer(h, word):
    # Write your code here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_dict = {}

    for i in range(len(alphabet)):
        alphabet_dict[alphabet[i]] = h[i]

    max_height = 0

    for i in word:
        if alphabet_dict[i] > max_height:
            max_height = alphabet_dict[i]

    return max_height * len(word)


# Solution 3
def designerPdfViewer(h, word):
    # Write your code here
    a = "abcdefghijklmnopqrstuvwxyz"

    maxHeight = 0
    for i in word:
        count = 0

        for j in a:
            if i == j:
                if maxHeight < h[count]:
                    maxHeight = h[count]
            else:
                count += 1

    return maxHeight * len(word)


# Input
h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word = "zaba"
print(designerPdfViewer(h, word))
