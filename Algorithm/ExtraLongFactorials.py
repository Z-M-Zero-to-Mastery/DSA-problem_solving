# The factorial of the integer n, written n!, is defined as:
#  n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
# Calculate and print the factorial of a given integer.

# For example, if n = 30, we calculate 30 * 29 * 28 * ... * 2 * 1 and get 265252859812191058636308480000000.
# Function Description Complete the extraLongFactorials function in the editor below. It should print the result and return. extraLongFactorials has the following parameter(s): n: an integer Constraints 1 <= n <= 100
#
# Note :Factorials of n > 20 can't be stored even in a 64-bit long long variable. Big integers must be used for such calculations. Languages like Java, Python, Ruby etc. can handle big integers, but we need to write additional code in C/C++ to handle huge values.

# We recommend solving this challenge using BigIntegers.

# Sample Input
# 25
# Sample Output
# 15511210043330985984000000

# Explanation
# 25! = 25 * 24 * 23 * ... * 3 * 2 * 1  = 15511210043330985984000000


# Solution: 1 (Using Recursion)
def extraLongFactorials(n):
    # Write your code here
    def fact(n):
        if n == 1:
            return 1

        return n * fact(n - 1)

    print(fact(n))


# Solution: 2 (Using Iteration)
def extraLongFactorials(n):
    # Write your code here
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    print(fact)


# Input:
n = int(input())
extraLongFactorials(n)
