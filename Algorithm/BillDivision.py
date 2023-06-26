# Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

# For example, assume the bill has the following prices: bill = [2, 4, 6] . Anna declines to eat item k = bill[2] which costs 6. If Brian calculates the bill correctly, Anna will pay (2+4)/2 = 3. If he includes the cost of biil[2], he will calculate (2+4+6)/2 = 6. In the second case, he should refund 3 to Anna.

# Sample Input 0
# 4 1
# 3 10 2 9
# 12

# Sample Output 0
# 5

# Explanation 0
# Anna didn't eat item bill[1] = 10, but she shared the rest of the items with Brian. The total cost of the shared items is 3+2+9 = 14 and, split in half, the cost per person is bactual = 7. Brian charged her bcharged = 12 for her portion of the bill. We print the amount Anna was overcharged, bcharged - bactual = 12 - 7 = 5, on a new line.

# Sample Input 1
# 4 1
# 3 10 2 9
# 7

# Sample Output 1
# Bon Appetit

# Explanation 1
# Anna didn't eat item bill[1] = 10, but she shared the rest of the items with Brian. The total cost of the shared items is 3+2+9 = 14 and, split in half, the cost per person is bactual = 7. Because bactual = bcharged = 7, we print Bon Appetit on a new line.

# Solution:


def bonAppetit(bill, k, b):
    total = 0
    # It is not necessary to use for loop here, we can use sum() function instead
    for i in range(len(bill)):
        # It checks if the index is not equal to k, then add the value to total
        if i != k:
            total += bill[i]

    # It checks if the total is equal to b, then print Bon Appetit
    if total // 2 == b:
        print("Bon Appetit")
    else:
        # It prints the difference between b and total//2
        print(int(b - total // 2))


# Solution 2:


def bonAppetit(bill, k, b):
    total = sum(bill)
    # It removes the value of bill[k] from total
    total -= bill[k]
    # It checks if the total is equal to b, then print Bon Appetit
    if total // 2 == b:
        print("Bon Appetit")
    else:
        # It prints the difference between b and total//2
        print(int(b - total // 2))


# Solution 3:


def bonAppetit(bill, k, b):
    total = sum(bill)
    # It removes the value of bill[k] from total
    total -= bill[k]
    # It checks if the total is equal to b, then print Bon Appetit
    print("Bon Appetit" if total // 2 == b else int(b - total // 2))


# Input

bill = [3, 10, 2, 9]
k = 1
b = 12
bonAppetit(bill, k, b)
