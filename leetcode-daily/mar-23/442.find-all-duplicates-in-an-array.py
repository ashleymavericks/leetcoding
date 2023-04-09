#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array (using constant memory)
#
# Approach: A neat trick of using array values as indices and treat them as on/off switch or +ve/-ve switch so that once you come to a -ve value again, means some duplicate value is trying to turn the switch back on.
# Time: O(n) , Space: O(1) -> constant memory

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            abs_value = abs(num)
            if nums[abs_value - 1] < 0:
                res.append(abs_value)
            else:
                nums[abs_value-1] = -nums[abs_value-1]
        return res

        
# @lc code=end

