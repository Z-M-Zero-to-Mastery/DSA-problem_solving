# You have two strings of lowercase English letters. You can perform two types of operations on the first string:

# 1 Append a lowercase English letter to the end of the string.
# 2 Delete the last character of the string. Performing this operation on an empty string results in an empty string.

# Given an integer, k, and two strings, s and t, determine whether or not you can convert s to t by performing exactly k of the above operations on s. If it's possible, print Yes. Otherwise, print No.

# Example s = [a,b,c] t = [d,e,f] k = 6
# To convert s to t, we first delete all of the characters in 3 moves. Next we add each of the characters of t in order. On the 6th move, you will have the matching string. Return Yes.
# If there were more moves available, they could have been eliminated by performing multiple deletions on an empty string. If there were fewer than 6 moves, we would not have succeeded in creating the new string.

# Function Description : Complete the appendAndDelete function in the editor below. It should return a string, either Yes or No. appendAndDelete has the following parameter(s):
# s: the initial string
# t: the desired string
# k: an integer that represents the number of operations

# Sample Input 0 : hackerhappy, hackerrank, 9
# Sample Output 0 : Yes
# Explanation 0 : We perform 5 delete operations to reduce string s to hacker. Next, we perform 4 append operations (i.e., r, a, n, and k), to get hackerrank. Because we were able to convert s to t by performing exactly k = 9 operations, we print Yes.

# Sample Input 1 : aba, aba, 7
# Sample Output 1 : Yes
# Explanation 1 : We perform 4 delete operations to reduce string s to the empty string (recall that, though the string will be empty after 3 deletions, we can still perform a delete operation on an empty string to get the empty string). Next, we perform 3 append operations (i.e., a, b, and a). Because we were able to convert s to t by performing exactly k = 7 operations, we print Yes.

# Sample Input 2 : ashley, ash, 2
# Sample Output 2 : No
# Explanation 2 : To convert ashley to ash a minimum of 3 steps are needed. Hence we print No as answer.


# Solution: 1
def appendAndDelete(s, t, k):
    count = 0

    # It will iterate through the string and count the number of matching characters
    for i, j in zip(s, t):
        if i == j:
            count += 1
        else:
            break

    # totalSize will be the sum of the length of both strings
    # eg: s = 'abc' and t = 'def' then totalSize = 6
    totalSize = len(s) + len(t)

    # if totalSize is less than 2*count+k and totalSize is even and k is even or totalSize is less than k then it will return 'Yes'
    # eg : s = 'abc' and t = 'def' and k = 6 then totalSize = 6 and count = 0
    # 6 < 2*0+6 and 6 is even and 6 is even or 6 < 6 then it will return 'Yes'
    # eg : s = 'ashley' and t = 'ash' and k = 2 then totalSize = 8 and count = 3
    # 9 <= 2*3+2 which is false and 9 is odd and 2 is even or 9 < 2 which is false then it will return 'No'
    if totalSize <= 2 * count + k and totalSize % 2 == k % 2 or totalSize < k:
        return "Yes"

    else:
        return "No"


# Solution: 2
def appendAndDelete(s, t, k):
    # Write your code here
    # Case 1 : If the sum of the length of both strings is less than k then it will return 'Yes'
    if len(s) + len(t) < k:
        return "Yes"
    # Case 2 : If the sum of the length of both strings is greater than k and the length of both strings is equal then it will return 'Yes'
    else:
        count = 0

        # It will iterate through the string and count the number of matching characters, it will iterate through the minimum length of both strings
        for i in range(min(len(s), len(t))):
            if s[i] == t[i]:
                count += 1
            else:
                break

        # Here we are subtracting the sum of the length of both strings and twice the count of matching characters from k
        # eg : s = 'ashley' and t = 'ash' and k = 2 then totalSize = 9 and count = 3  and 9 + 3 - 2*3 = 3
        # 3 is less than 2 which is false and 3 is odd and 2 is even or 3 < 2 which is false then it will return 'No'
        if (len(s) + len(t) - 2 * count) > k:
            return "No"

        # Here we are checking if the sum of the length of both strings and twice the count of matching characters is even and k is even or the sum of the length of both strings and twice the count of matching characters is odd and k is odd then it will return 'Yes'
        # eg : s = 'abc' and t = 'def' and k = 6 then totalSize = 6 and count = 0
        # 6 < 2*0+6 and 6 is even and 6 is even or 6 < 6 then it will return 'Yes'
        elif (len(s) + len(t) - 2 * count) % 2 == k % 2:
            return "Yes"

        #  Here we are checking if the sum of the length of both strings and twice the count of matching characters is less than 0 then it will return 'Yes'
        elif (len(s) + len(t) - k) < 0:
            return "Yes"

        else:
            return "No"


# Input
s = input()
t = input()
k = int(input())

print(appendAndDelete(s, t, k))
