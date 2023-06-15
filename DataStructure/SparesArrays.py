# There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

# Example
# strings = ['ab', 'ab', 'abc']
# queries = ['ab', 'abc', 'bc']

# There are 2 instances of 'ab',  of 1 'abc' and 0 of 'bc'. For each query, add an element to the return array, result = [2, 0, 1] .


# Solution 1:
def matchingStrings(strings, queries):
    result = []
    for i in queries:
        result.append(strings.count(i))
    return result


# Solution 2:
def matchingStrings(strings, queries):
    result = []
    for i in queries:
        count = 0
        for j in strings:
            if i == j:
                count += 1
        result.append(count)
    return result


# Solution 3:
# Using dictionary
def matchingStrings(strings, queries):
    result = []
    dict = {}
    for i in strings:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in queries:
        if i in dict:
            result.append(dict[i])
        else:
            result.append(0)
    return result


# Solution 4:
# Using dictionary
def matchingStrings(strings, queries):
    result = []
    dict = {}
    for i in strings:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in queries:
        result.append(dict.get(i, 0))
    return result


# Solution 5:
# Using dictionary
def matchingStrings(strings, queries):
    result = []
    dict = {}
    for i in strings:
        dict[i] = dict.get(i, 0) + 1
    for i in queries:
        result.append(dict.get(i, 0))
    return result


# input
strings = ["ab", "ab", "abc"]
queries = ["ab", "abc", "bc"]

matchingStrings(strings, queries)
