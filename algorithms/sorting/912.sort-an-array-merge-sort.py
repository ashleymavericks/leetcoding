# @before-stub-for-debug-begin
from python3problem912 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) > 1:
            mid = len(nums) // 2
            l = nums[:mid]
            r = nums[mid:]

            self.sortArray(l)
            self.sortArray(r)

            i = j = k = 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    nums[k] = l[i]
                    i += 1
                else:
                    nums[k] = r[j]
                    j += 1
                k += 1
            # for the remaining elements
            while i < len(l):
                nums[k] = l[i]
                i, k = i+1, k+1
            while j < len(r):
                nums[k] = r[j]
                j, k = j+1, k+1
        return nums
        
# @lc code=end

