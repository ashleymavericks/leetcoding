#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# Approach: keep dividing the numsay into smaller chunk by the factor of 2
# Time: O(logn) -> base 2 , Space: O(1)

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left+right)//2

            """ to prevent overflow situation with 2^31 order numbers in other languages, basically taking the half distance between the numbers and adding it to the left """
            # middle = left + ((right-left)//2)

            if target > nums[middle]:
                left = middle+1
            elif target < nums[middle]:
                right = middle-1
            else:
                return middle
        else:
            return -1
        
# @lc code=end

