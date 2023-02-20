# @before-stub-for-debug-begin
from python3problem50 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# Approach: Binary Exponentiation ->Square the base & divide the exponent by 2, 2^8 = 4^2 = 16^2 = 256^1
# Time: O(logn) , Space: O(1)

# @lc code=start
# Iterative approach
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n == 0:
            return 1
        y = abs(n)
        while y > 1:
            if y % 2 == 0:
                y //= 2
                x *= x
            else:
                res = res * x
                y -= 1
        res = res * x
        return 1/res if n < 0 else res


# Recursive approach
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            # base cases
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x * x, n // 2)
            # res = helper(x, n // 2)
            # res = res * res
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return 1/res if n < 0 else res

# @lc code=end
