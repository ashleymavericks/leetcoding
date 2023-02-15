#
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high-low)//2 if (high % 2)==0 and (low % 2)==0 else (high-low)//2 + 1
        
# @lc code=end

