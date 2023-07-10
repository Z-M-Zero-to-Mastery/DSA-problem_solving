# A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time (arrivalTime <= 0) to arrived late (arrivalTime > 0).

# Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.

# Example
# n = 5
# k = 3
# a = [-2, -1, 0, 1, 2]
# The first 3 students arrived on. The last 2 were late. The threshold is 3 students, so class will go on. Return YES.

# NOTE: Non-positive arrival times (a[i] <= 0) indicate the student arrived early or on time; positive arrival times (a[i] > 0) indicate the student arrived a[i] minutes late.

# Return YES if class is cancelled, or NO otherwise.

# Sample Input
# 2
# 4 3
# -1 -3 4 2
# 4 2
# 0 -1 2 1

# Sample Output
# YES
# NO

# Explanation
# For the first test case, k = 3. The professor wants at least 3 students in attendance, but only 2 have arrived on time (-3 and -1). Thus, the class is cancelled. For the second test case, k = 2. The professor wants at least 2 students in attendance, and there are 2 who have arrived on time (0 and -1). Thus, the class is not cancelled.


# Solution
def angryProfessor(k, a):
    count = 0

    for i in a:
        # It will count the number of students who arrived on time or early
        if i <= 0:
            count += 1

    if count >= k:
        return "NO"
    else:
        return "YES"


# Input
k = 3
a = [-1, -3, 4, 2]

print(angryProfessor(k, a))
