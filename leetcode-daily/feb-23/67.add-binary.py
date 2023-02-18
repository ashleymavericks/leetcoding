#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# Approach: Use of mod 2 and integer division by 2 for binary addition cases
# Time: O(n) , Space: O(n)

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # reverse strings to prevent O(n) complexity from start of array addition
        a = a[::-1]
        b = b[::-1]
        res = ''
        carry = 0

        for i in range(max(len(a), len(b))):
            digit1 = 0 if i >= len(a) else int(a[i])
            digit2 = 0 if i >= len(b) else int(b[i])
            total = digit1 + digit2 + carry
            add = total % 2  # for binary addition
            res = str(add) + res
            carry = total // 2  # for carry
        if carry:
            res = '1' + res
        return res
    
# @lc code=end

