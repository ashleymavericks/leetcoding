# @before-stub-for-debug-begin
from python3problem35 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# Approach: Same as binary search but here return leftPointer at the end
# Time: O(logn) , Space: O(1)

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return left

# @lc code=end
