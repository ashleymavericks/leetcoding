#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#
# Approach: Simply keeping two pointers
# Time: O(n) , Space: O(1) - Constant Space

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        count = 0
        for i in range(len(t)):
            if s[count] == t[i]:
                count += 1
                if count == len(s):
                    return True
        return False
        
# @lc code=end

