# Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

# Example
# scores = [12,24,10,24]
# Scores are in the same order as the games played. She tabulates her results as follows:

# game  score  minimum  maximum   min max
#  0      12     12       12       0   0
#  1      24     12       24       0   1
#  2      10     10       24       1   1
#  3      24     10       24       1   1

# Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.
# Sample Input 0

# 9
# 10 5 20 20 4 5 2 25 1
# Sample Output 0

# 2 4
# Explanation 0

# game  score  minimum  maximum   min max
#  0      10     10       10       0   0
#  1      5      5        10       1   1
#  2      20     5        20       1   2
#  3      20     5        20       1   2
#  4      4      4        20       2   2
#  5      5      4        20       2   2
#  6      2      2        20       3   2
#  7      25     2        25       3   3
#  8      1      1        25       4   3
# She broke her best record twice (after games 2 and 7) and her worst record four times (after games 1, 4, 6, and 8), so we print 2 4 as our answer. Note that she did not break her record for best score during game 3, as her score during that game was not strictly greater than her best record at the time.

# Solution:


def breakingRecords(scores):
    # Write your code here
    min = max = scores[0]
    min_count = max_count = 0

    for i in range(1, len(scores)):
        if scores[i] > max:
            max = scores[i]
            max_count += 1

        if scores[i] < min:
            min = scores[i]
            min_count += 1

    return max_count, min_count


if __name__ == "__main__":
    scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    result = breakingRecords(scores)
    print(result)
