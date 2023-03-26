# @before-stub-for-debug-begin
from python3problem540 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#
# Approach: Modified Binary Search
# Time: O(logn) , Space: O(1)

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # m = (l + r) // 2  ## potential memory overflow bug
            m = l + ((r - l) // 2)

            if ((m - 1 < 0 or nums[m-1] != nums[m]) and
                    (m + 1 == len(nums) or nums[m] != nums[m+1])):
                return nums[m]

		# post introduction of single pair element, pair indices change from (even,odd) -> (odd,even)
            if nums[m-1] == nums[m]:
                if m % 2:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[m] == nums[m + 1]:
                if not m % 2:
                    l = m + 1
                else:
                    r = m - 1
                    
# Another way with similar time and space complexity
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # m = (l + r) // 2  ## potential memory overflow bug
            m = l + ((r - l) // 2)

            if ((m - 1 < 0 or nums[m-1] != nums[m]) and
                    (m + 1 == len(nums) or nums[m] != nums[m+1])):
                return nums[m]

            # side with unpaired element will have odd numbers of values
            left_size = m - 1 if nums[m - 1] == nums[m] else m
            if left_size % 2:
                r = m - 1
            else:
                l = m + 1
        
# @lc code=end

