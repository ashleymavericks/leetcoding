#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        # current window trackers in which BFS will perform
        l = r = 0

        while r < len(nums) - 1:  # until reaches the last value of input array
            farthest = 0
            # to check which element can jump the farthest
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
                # incrementing left pointer to right + 1 and right pointer to the farthest to create the new section
            l = r + 1
            r = farthest
            jumps += 1
        return jumps
        
# @lc code=end

