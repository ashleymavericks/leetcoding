# @before-stub-for-debug-begin
from python3problem20 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# Approach: Use stack data structure, also need to validate nested parentheses
# Time: O(n) , Space: O(n)

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
        
# @lc code=end

