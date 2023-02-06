#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # prefix sum
        for n in range(1, len(nums)):
            nums[n] += nums[n-1]
        return nums
# @lc code=end

