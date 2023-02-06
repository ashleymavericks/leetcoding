#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#
# Approach: Analyse the pattern and create mathematical forumula to cover each value, based on how many hops will be needed to reach to the next

# Time: O(n^2) , Space: O(1)

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        pattern = ''

        for r in range(numRows):
            increment = (numRows - 1) * 2
            for j in range(r, len(s), increment):
                pattern += s[j]
                # to cover the extra values of in-between rows /  middle rows
                if (r > 0 and r < numRows - 1 and
                        j + increment - 2 * r < len(s)):  # to check if 6-2r index is inbound
                    pattern += s[j + increment - 2 * r]

        return pattern
        
# @lc code=end

