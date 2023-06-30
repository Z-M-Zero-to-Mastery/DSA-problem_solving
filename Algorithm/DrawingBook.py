# A teacher asks the class to open their books to a page number. A student can either start turning pages from the front of the book or from the back of the book. They always turn pages one at a time. When they open the book, page 1 is always on the right side:
# When they flip page 1, they see pages 2 and 3. Each page except the last page will always be printed on both sides. The last page may only be printed on the front, given the length of the book.
# If the book is n pages long, and a student wants to turn to page p, what is the minimum number of pages to turn? They can start at the beginning or the end of the book.
# Given n and p, find and print the minimum number of pages that must be turned in order to arrive at page p.

# Example
# n = 5
# p = 3

# If the student wants to get to page 3, they open the book to page 1, flip 1 page and they are on the correct page. If they open the book to the last page, page 5, they turn 1 page and are at the correct page. Return 1.

# Sample Input 0
# 6
# 2

# Sample Output 0
# 1

# Sample Input 1
# 5
# 4

# Sample Output 1
# 0

# Explanation 1
# If the student wants to get to page 4, they turn 2 pages and are at the correct page. If they open the book to the last page, page 5, they turn 1 page and are on the correct page. Return 0.


# Solution 1:
def pageCount(n, p):
    # Here we are finding the minimum number of pages to turn to reach the page p
    # eg n = 6, p = 2 => 1
    if n % 2 == 0:
        # if n is even
        # if p is less than or equal to half of n
        # 2 is less than or equal to 3
        if p <= n / 2:
            # 2//2 = 1
            return p // 2
        else:
            # if p is greater than half of n
            # eg p = 5 and n = 6
            # 6-5 = 1 => 1//2 = 0
            return (n - p) // 2

    # if n is odd
    else:
        # if p is less than or equal to half of n
        # eg : p = 3 and n = 5
        # 3 <= 5/2 => 3 <= 2.5 => False
        if p <= n / 2:
            return p // 2
        # if p is greater than half of n
        else:
            # eg : p = 4 and n = 5
            # 5-4 = 1 => 1//2 = 0
            return (n - p) // 2


# Solution 2: (Using Math)
def pageCount(n, p):
    # Here we are finding the minimum number of pages to turn to reach the page p from the front or back
    front = p // 2

    # if n is odd
    # eg : n = 5 and p = 4
    if n % 2 == 1:
        # 5-4 = 1 => 1//2 = 0
        back = (n - p) // 2
    # if n is even
    # eg : n = 6 and p = 4
    else:
        # 6-4+1 = 3 => 3//2 = 1
        back = (n - p + 1) // 2

    return min(front, back)


# Solution 3: Using list comprehension
def pageCount(n, p):
    # Here we are finding the minimum number of pages to turn to reach the page p from the front or back
    front = [i for i in range(0, p, 2)]
    back = [i for i in range(n, p, -2)]

    return min(len(front), len(back))


# Input
n = 6
p = 2
print(pageCount(n, p))
