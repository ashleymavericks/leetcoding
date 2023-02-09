#
# @lc app=leetcode id=1626 lang=python3
#
# [1626] Best Team With No Conflicts
#

# @lc code=start
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = [[scores[i], ages[i]] for i in range(len(scores))]
        pairs.sort()  # scores in ascending order
        dp = [pairs[i][0] for i in range(len(pairs))]  # scores

        # considering i is the max value, what max possible score we can get
        for i in range(len(pairs)):
            mScore, mAge = pairs[i]
            # for every value to the left of i (since we considering it max)
            for j in range(i):
                score, age = pairs[j]
                # if age of high scorer is >= age of person with <= score
                if mAge >= age:
                    dp[i] = max(dp[i], mScore + dp[j])
        return max(dp)

# @lc code=end

