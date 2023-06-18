# Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, determine the number of apples and oranges that land on Sam's house.
# In the diagram below:
# The red region denotes the house, where s is the start point, and t is the endpoint. The apple tree is to the left of the house, and the orange tree is to its right.
# Assume the trees are located on a single point, where the apple tree is at point a, and the orange tree is at point b.
# When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis. *A negative value of d means the fruit fell d units to the tree's left, and a positive value of d means it falls d units to the tree's right. *

# Given the value of d for m apples and n oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range [s,t])?

# For example, Sam's house is between s=7 and t=10. The apple tree is located at a=4 and the orange at b=12. There are m=3 apples and n=3 oranges. Apples are thrown apples=[2,3,-4] units distance from a, and oranges=[3,-2,-4] units distance. Adding each apple distance to the position of the tree, they land at [4+2,4+3,4+-4]=[6,7,0]. Oranges land at [12+3,12+-2,12+-4]=[15,10,8]. One apple and two oranges land in the inclusive range 7-10 so we print
# 1
# 2

# Sample Input 0
# 7 11
# 5 15
# 3 2
# -2 2 1
# 5 -6

# Sample Output 0
# 1
# 1

# Explanation 0
# The first apple falls at position 5-2=3.
# The second apple falls at position 5+2=7.
# The third apple falls at position 5+1=6.

# The first orange falls at position 15+5=20.
# The second orange falls at position 15-6=9.

# Only one fruit (the second apple) falls within the region between 7 and 11, so we print 1 as our first line of output.

# Only the second orange falls within the region between 7 and 11, so we print 1 as our second line of output.


# Solution 1:
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    appleCount = 0
    orangeCount = 0

    # This loop is for apples
    for apple in apples:
        # This if statement is for checking if the apple is in the range of s and t
        if a + apple >= s and a + apple <= t:
            appleCount += 1

    # This loop is for oranges
    for orange in oranges:
        # This if statement is for checking if the orange is in the range of s and t
        if b + orange >= s and b + orange <= t:
            orangeCount += 1
    print(appleCount)
    print(orangeCount)


# Solution 2:
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    appleCount = 0
    orangeCount = 0
    for apple in apples:
        if a + apple in range(s, t + 1):
            appleCount += 1
    for orange in oranges:
        if b + orange in range(s, t + 1):
            orangeCount += 1
    print(appleCount)
    print(orangeCount)


# Solution 3:
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    appleCount = 0
    orangeCount = 0
    for apple in apples:
        if s <= a + apple <= t:
            appleCount += 1
    for orange in oranges:
        if s <= b + orange <= t:
            orangeCount += 1
    print(appleCount)
    print(orangeCount)
