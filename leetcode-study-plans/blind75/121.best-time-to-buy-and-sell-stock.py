# @before-stub-for-debug-begin
from python3problem121 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        l, r = 0, 1  # left=buy, right=sell
        while r < len(prices):
            if prices[l] > prices[r]:
                # slide through the whole window as max achieved for this window and we found a new low buying price
                l = r
            else:
                max_price = max(prices[r] - prices[l], max_price)
            r += 1
        return max_price
        
# @lc code=end

