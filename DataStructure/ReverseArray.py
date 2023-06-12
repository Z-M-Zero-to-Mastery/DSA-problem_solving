# An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, A , of size N, each memory location has some unique index,  i(where 0 < i < N), that can be referenced as A[i]  or Ai.

# Reverse an array of integers.
# Example 
# A = [1,2,3]
# Return [3,2,1]

# Solution 1:

def reverseArray(a):
    return a[::-1]

# Solution 2:
def reverseArray(a):
    return list(reversed(a))

# solution 3:
def reverseArray(a):
    a.reverse()
    return a

a = [1,2,3]
print(reverseArray(a))