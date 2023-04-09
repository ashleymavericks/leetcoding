#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number (in immutable array using constant memory)
#
# Approach: Floyd's Circle Algorithm in case of immutable array
# Time: O(n) , Space: O(1)

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        
# @lc code=end

