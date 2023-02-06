#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#
# Approach: Prefix sum + Leveraging the total sum of array which is constant.
# Time: O(n) , Space: O(1)

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # O(n) , its okay because our algorithm does run  in O(n) anyway
        total_sum = sum(nums)
        left_sum = 0
        for n in range(len(nums)):
            if left_sum == total_sum - nums[n] - left_sum:
                return n
            left_sum += nums[n]
        return -1
        
# @lc code=end

