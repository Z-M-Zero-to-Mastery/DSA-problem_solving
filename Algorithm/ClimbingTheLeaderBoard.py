# An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

# The player with the highest score is ranked number 1 on the leaderboard.
# Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

# Example
# ranked = [100,90,90,80]
# player = [70,80,105]

# The ranked players will have ranks 1,2,2,3 respectively. If the player's scores are 70,80 and 105, their rankings after each game are 4th,3rd and 1st. Return [4,3,1].

# Returns an integer array containing the ranks of each player after each game.

# Sample Input 0
# 7
# 100 100 50 40 40 20 10
# 4
# 5 25 50 120

# Sample Output 0
# 6
# 4
# 2
# 1

# Explanation 0

# Alice starts playing with 7 players already on the leaderboard, which looks like this:
# Rank Score          Rank   Score
# 1   100             1      100
# 1   100             1      100
# 2   50     ----->   2      50
# 3   40              3      40
# 3   40              3      40
# 4   20              4      20
# 5   10              5      10
#                     6      5 (Rank)
# After Alice finishes game 0, her score is 5 and her ranking is 6:
# Rank Score          Rank   Score
# 1      100          1      100
# 1      100          1      100
# 2      50           2      50
# 3      40  ------>  3      40
# 3      40           3      40
# 4      20           4      25 (Rank)
# 5      10           5      20
# 6      5            6      10

# After Alice finishes game 1, her score is 25 and her ranking is 4:
# Rank Score          Rank   Score
# 1      100          1      100
# 1      100          1      100
# 2      50           2      50
# 3      40  ------>  2      50 (Rank)
# 3      40           3      40
# 4      25           3      40
# 5      20           5      20
# 6      10           6      10

# After Alice finishes game 2, her score is 50 and her ranking is tied with Caroline at 2:
# This will continue for games 3 and 4 as Alice's all three scores equal to 50 and her ranking is tied with Caroline at 2.
# Return [6,4,2,1].


# Solution 1:
def climbingLeaderboard(ranked, player):
    # This solution is not efficient for large data sets
    # The ranked list is sorted and duplicates are removed
    # eg ranked = [100,90,90,80] -> [100,90,80]
    ranked = sorted(list(set(ranked)), reverse=True)
    player_rank = []

    for i in player:
        # The player score is appended to the ranked list
        ranked.append(i)
        # The ranked list is sorted and duplicates are removed
        # i is the player score = (70)
        # eg ranked = [100,90,80,70] -> [100,90,80,70]
        ranked = sorted(list(set(ranked)), reverse=True)
        # The player rank is appended to the player_rank list
        player_rank.append(ranked.index(i) + 1)

    return player_rank


# Solution 2:
def climbingLeaderboard(ranked, player):
    # Write your code here
    arr = []
    # The ranked list is sorted and duplicates are removed
    ranked = list(set(ranked))
    ranked.sort()
    # ranked = [10,20,40,50,100]
    n = len(ranked)
    i = 0

    # The player score is compared to the ranked list
    for score in player:
        # The player score is compared to the ranked list
        # If the player score is greater than the ranked score then the player rank is appended to the arr list
        # eg player = [5,25,50,120]
        # 10 <= 5 this is false so the loop continues
        while i < n and ranked[i] <= score:
            i += 1

        # The player rank is appended to the arr list
        # eg ranked = [10,20,40,50,100]
        # 10 < 5 this is false so the loop continues so i = 0, n = 5, n - i + 1 = 6 so 6 is appended to the arr list
        # in the second iteration 10 <= 25 (true) i = 1, 20 <= 25 (true) i = 2, 40 <= 25 (false) i = 2, n = 5, n - i + 1 = 4 so 4 is appended to the arr list
        arr.append(n - i + 1)

    return arr


# Input

ranked = [100, 90, 90, 80]
player = [70, 80, 105]

print(climbingLeaderboard(ranked, player))
