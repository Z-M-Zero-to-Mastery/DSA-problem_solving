# Staircase detail

# This is a staircase of size : n = 4

#    #
#   ##
#  ###
# ####

# Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

# Solution 1:

def staircase(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"#"*i)

# Solution 2:

def staircase(n):
    for i in range(1,n+1):
        print(("#"*i).rjust(n))

# Solution 3:

def staircase(n):
    
    for i in range(n):

        for j in range(n-i-1):
            print(" ", end="")

        for j in range(i+1):
            print("#", end="")

        print()

# Input
# 6
staircase(6)