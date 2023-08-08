# There are a number of people who will be attending ACM-ICPC World Finals. Each of them may be well versed in a number of topics. Given a list of topics known by each attendee, presented as binary strings, determine the maximum number of topics a 2-person team can know. Each subject has a column in the binary string, and a '1' means the subject is known while '0' means it is not. Also determine the number of teams that know the maximum number of topics. Return an integer array with two elements. The first is the maximum number of topics known, and the second is the number of teams that know that number of topics.

# Example
# n = 3
# topics = ['10101', '11100', '11010']
# The attendee data is aligned for clarity below:
# 10101
# 11100
# 11010
# These are all possible teams that can be formed:
# Members Subjects
# (1,2)   [1,2,3,4,5]
# (1,3)   [1,3,4,5]
# (2,3)   [1,2,3,4]
# In this case, the first team will know all 5 subjects. They are the only team that can be created that knows that many subjects, so [5, 1] is returned.

# Returns : int[2]: the maximum topics and the number of teams that know that many topics

# Sample Input
# 4
# 10101
# 11100
# 11010
# 00101

# Sample Output
# 5
# 2

# Explanation
# Calculating topics known for all permutations of 2 attendees we get:
# (1,2) -> 4
# (1,3) -> 5
# (1,4) -> 3
# (2,3) -> 5
# (2,4) -> 4
# (3,4) -> 5
# The 2 teams (1, 3) and (3, 4) know all 5 topics which is maximal.


# Solution: 1 - Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def acmTeam(topic):
    # Create a list to store the number of topics known by each team
    topics_known = []

    # Create a list to store the number of teams that know the maximum number of topics
    teams = []

    # Iterate through the list of topics
    for i in range(len(topic)):
        # Iterate through the list of topics again
        for j in range(i + 1, len(topic)):
            # Create a variable to store the number of topics known by each team
            topics = 0

            # Iterate through the list of topics
            for k in range(len(topic[i])):
                # If the topic is known by either team, increment the number of topics
                if topic[i][k] == "1" or topic[j][k] == "1":
                    topics += 1

            # Append the number of topics known by each team to the list
            topics_known.append(topics)

    # Append the maximum number of topics known by a team to the list
    teams.append(max(topics_known))

    # Append the number of teams that know the maximum number of topics to the list
    teams.append(topics_known.count(max(topics_known)))

    # Return the list
    return teams


# Solution: 2 Using Bitwise Operators (Optimized)


def acmTeam(topic):
    # Initialize a variable to store the maximum number of topics known by a team
    maxsub = 0
    count = 0

    # Iterate through the list of topics
    for i in range(len(topic)):
        # Iterate through the list of topics again
        for j in range(i + 1, len(topic)):
            # Create a variable to store the number of topics known by each team using bitwise OR operator
            # Count the number of 1's in the binary representation of the number
            # Eg: 10101 | 11100 = 11101 -> 4
            sub = bin(int(topic[i], 2) | int(topic[j], 2)).count("1")

            # If the number of topics known by a team is greater than the maximum number of topics known by a team so far, update the maximum number of topics known by a team and reset the count  to 1
            # eg: 4 > 0 -> maxsub = 4, count = 1
            if sub > maxsub:
                maxsub = sub
                count = 1

            # If sub is equal to maxsub, increment the count
            # eg: 4 == 4 -> count = 2
            elif sub == maxsub:
                count += 1

    return [maxsub, count]


# **********************************************OR***************************************************
def acmTeam(topic):
    maxsub = 0
    count = 0

    for i in range(len(topic)):
        for j in range(i + 1, len(topic)):
            sub = 0

            # Iterate through the list of topics using zip function to iterate through the list of topics simultaneously
            # topic[i] = '10101' and topic[j] = '11100' -> zip(topic[i], topic[j]) = [('1', '1'), ('0', '1'), ('1', '1'), ('0', '0'), ('1', '0')]
            for x, y in zip(topic[i], topic[j]):
                if x == "1" or y == "1":
                    sub += 1

            if sub > maxsub:
                maxsub = sub
                count = 1
            elif sub == maxsub:
                count += 1

    return [maxsub, count]


# Solution: 3 Using Combinations
# Time Complexity: O(n^2)
# Space Complexity: O(n)
from itertools import combinations


def acmTeam(topic):
    # Create a list to store the number of topics known by each team
    topics_known = []

    # Create a list to store the number of teams that know the maximum number of topics
    teams = []

    # Iterate through the list of topics
    for i in list(combinations(range(len(topic)), 2)):
        # Create a variable to store the number of topics known by each team
        topics = 0

        # Iterate through the list of topics
        for j in range(len(topic[i[0]])):
            # If the topic is known by either team, increment the number of topics
            if topic[i[0]][j] == "1" or topic[i[1]][j] == "1":
                topics += 1

        # Append the number of topics known by each team to the list
        topics_known.append(topics)

    # Append the maximum number of topics known by a team to the list
    teams.append(max(topics_known))

    # Append the number of teams that know the maximum number of topics to the list
    teams.append(topics_known.count(max(topics_known)))

    # Return the list
    return teams


# Solution: 4 Using Dictionary
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def acmTeam(topic):
    # Create a dictionary to store the number of topics known by each team
    topics_known = {}

    # Create a list to store the number of teams that know the maximum number of topics
    teams = []

    # Iterate through the list of topics
    for i in range(len(topic)):
        # Iterate through the list of topics again
        for j in range(i + 1, len(topic)):
            # Create a variable to store the number of topics known by each team
            topics = 0

            # Iterate through the list of topics
            for k in range(len(topic[i])):
                # If the topic is known by either team, increment the number of topics
                if topic[i][k] == "1" or topic[j][k] == "1":
                    topics += 1

            # If the number of topics known by each team is not in the dictionary, add it to the dictionary
            if topics not in topics_known:
                topics_known[topics] = 1

            # If the number of topics known by each team is in the dictionary, increment the value by 1
            else:
                topics_known[topics] += 1

    # Append the maximum number of topics known by a team to the list
    teams.append(max(topics_known))

    # Append the number of teams that know the maximum number of topics to the list
    teams.append(topics_known[max(topics_known)])

    # Return the list
    return teams


# Input

topic = ["10101", "11100", "11010", "00101"]

print(acmTeam(topic))
