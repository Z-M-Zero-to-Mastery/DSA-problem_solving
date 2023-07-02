# A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return -1.
# Example
# b = 60
# keyboards = [40,50,60]
# drives = [5,8,12]
# The person can buy a 40 keyboard + 12 USB drive = 52, or a 50 keyboard + 8 USB drive = 58. Choose the latter as the more expensive option and return 58.

# Return the maximum total price for the two items within the given budget, or -1 if you cannot afford both items.
# Sample Input 0
# 10 2 3
# 3 1
# 5 2 8
# Sample Output 0
# 9
# Explanation 0
# Buy the 2nd keyboard and the 3rd USB drive for a total cost of 8+1=9.

# Sample Input 1
# 5 (1 1) (len of keyboards and drives)
# 4
# 5
# Sample Output 1
# -1

# Explanation 1
# There is no way to buy one keyboard and one USB drive because 4+5>5, so return -1.


# Solution: 1
def getMoneySpent(keyboards, drives, b):
    # Write your code here.
    max = -1

    for i in keyboards:
        for j in drives:
            # Here condition is i+j <= b because we have to find the maximum price of keyboard and drive which is less than or equal to b
            if i + j <= b and i + j > max:
                max = i + j
    return max


# Solution: 2 (Using List Comprehension)
def getMoneySpent(keyboards, drives, b):
    # Write your code here.
    return max(
        [sum([x, y]) for x in keyboards for y in drives if sum([x, y]) <= b] + [-1]
    )


# Solution: 3 Using List
def getMoneySpent(keyboards, drives, b):
    ar = []

    for i in keyboards:
        total = 0
        for j in drives:
            total = i + j
            if total <= b:
                ar.append(total)

    if len(ar) == 0:
        return -1
    else:
        return max(ar)


# Solution: 4 Using Dictionary
def getMoneySpent(keyboards, drives, b):
    ar = {}

    for i in keyboards:
        total = 0
        for j in drives:
            total = i + j
            if total <= b:
                ar[total] = total

    if len(ar) == 0:
        return -1
    else:
        return max(ar)


# Input
keyboards = [3, 1]
drives = [5, 2, 8]
b = 10
print(getMoneySpent(keyboards, drives, b))
