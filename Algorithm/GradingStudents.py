# HackerLand University has the following grading policy:

# Every student receives a grade in the inclusive range 0 from 100  to .
# Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's grade according to these rules:

# If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

# Examples
# grade = 84 round to 85 (85 - 84 is less than 3)
# grade = 29 do not round (result is less than 40)
# grade = 57 do not round (60 - 57 is 3 or higher)

# Sample Input 0
# 4
# 73
# 67
# 38
# 33

# Sample Output 0
# 75
# 67
# 40
# 33

# Explanation 0
# image

# Student 1 received a 73, and the next multiple of 5 from 73 is 75. Since 75 - 73 < 3, the student's grade is rounded to 75.
# Student 2 received a 67, and the next multiple of 5 from 67 is 70. Since 70 - 67 = 3, the grade will not be modified and the student's final grade is 67.
# Student 3 received a 38, and the next multiple of 5 from 38 is 40. Since 40 - 38 < 3, the student's grade will be rounded to 40.
# Student 4 received a grade below 38, so the grade will not be modified and the student's final grade is 33.


# Solution 1:
def gradingStudents(grades):
    result = []

    for grade in grades:
        if grade >= 38:
            # Here we are checking the remainder of the grade when divided by 5
            # eg: 73 % 5 = 3
            # eg: 67 % 5 = 2
            mod5 = grade % 5

            # If the remainder is greater than or equal to 3, we need to round up
            if mod5 >= 3:
                # eg: 73 + (5 - 3) = 75
                grade += 5 - mod5
                result.append(grade)

        else:
            result.append(grade)

    return result


# Solution 2:
def gradingStudents(grades):
    g = []

    for i in grades:
        num = Math.ceil(i / 5)
        num = num * 5

        val = num - i
        if i >= 38:
            if val < 3:
                g.append(num)

            else:
                g.append(i)
        else:
            g.append(i)

    return g
