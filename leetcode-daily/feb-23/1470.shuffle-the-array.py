#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#
# Approach: Bit manipulation
# Time: O(n) , Space: O(1) -> Constant Space, didn't have to declare any extra data structure

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i] = nums[i] << 10  # shift the x values by 10 bits
            # store the y value by bitwise OR it with shifted x value
            nums[i] = nums[i] | nums[i + n]

        # iterate through the pairs in reverse order to avoid overriding the values
        j = 2 * n - 1
        for i in range(n - 1, -1, -1):
            # extract x & y values
            # extracting y value by bitwise AND it with (2**10 - 1, basically 10 times 1,1,1,.....)
            y = nums[i] & (2**10 - 1)
            x = nums[i] >> 10
            nums[j] = y
            nums[j - 1] = x
            j -= 2
        return nums
        
# @lc code=end

