# Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Taum: one is black and the other is white. To make her happy, Taum has to buy b black gifts and w white gifts.
# The cost of each black gift is bc units.
# The cost of every white gift is wc units.
# The cost of converting each black gift into white gift or vice versa is z units.
# Help Taum by deducing the minimum amount he needs to spend on Diksha's gifts.
# For example, if Taum wants to buy b=3 black gifts and w=5 white gifts at a cost of bc=3, wc=4 and conversion cost z=1, we see that he can buy a black gift for 3 and convert it to a white gift for 1, making the total cost of each white gift 4. That matches the cost of a white gift, so he can do that or just buy black gifts and white gifts. Either way, the overall cost is 3*3+5*4=29.

# Return the minimal cost of obtaining the desired gifts.

# Sample Input
# 10 10
# 1 1 1

# Sample Output
# 20

# Explanation :  There is no benefit to converting the white gifts into black or the black gifts into white, so Taum will have to buy each gift for 1 unit. The cost of buying all gifts will be: b*bc+w*wc=10*1+10*1=20.

# Sample Input
# 5 9
# 2 3 4

# Sample Output
# 37

# Explanation :  Again, we can't decrease the cost of black or white gifts by converting colors. bc=2, wc=3, and z=4, so cost(b=5,w=9,bc=2,wc=3,z=4)=5*2+9*3=10+27=37.

# Sample Input
# 3 6
# 9 1 1

# Sample Output
# 12

# Explanation :  We can convert each black gift to white gift at a cost of 1 unit each. taum will buy b=3 white gifts at a cost of w=1, and convert them to black gifts for z=1 unit. For gifts, we would spend 3*1+3*1=6, which is less than or equal to the cost of buying all white gifts and converting them to black gifts. bc=9, wc=1, and z=1, so cost(b=3,w=6,bc=9,wc=1,z=1)=3*9+6*1=27+6=33.


# Solution 1
def taumBday(b, w, bc, wc, z):
    # If the cost of converting is greater than the cost difference between the colors, then it is better to buy the gifts of the same color
    # It checks if it is better to buy the gifts of the same color and convert them to the other color
    if bc > wc + z:
        return (b + w) * wc + b * z
    elif wc > bc + z:
        return (b + w) * bc + w * z
    else:
        return b * bc + w * wc


# Solution 2
def taumBday(b, w, bc, wc, z):
    # It is always optimal to convert from the more expensive color to the cheaper one
    return min(b * bc + w * wc, b * bc + w * (bc + z), b * (wc + z) + w * wc)


# Input
b = 10
w = 10
bc = 1
wc = 1
z = 1

print(taumBday(b, w, bc, wc, z))
