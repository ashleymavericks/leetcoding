#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
#

# @lc code=start

# Approach: Leverage Python reverse indexing for string
# Time: O(n/2) , Space: O(1)

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # vowels = ('aeiouAEIOU')
        left, right = 0, 0
        for i in range(len(s)//2):
            if s[i] in vowels:
                left += 1
            if s[-i-1] in vowels:
                right += 1
        if left == right:
            return True
        else:
            return False
        
# @lc code=end

