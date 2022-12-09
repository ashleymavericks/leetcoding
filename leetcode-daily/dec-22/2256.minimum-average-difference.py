#16
# @lc app=leetcode id=2256 lang=python3
#
# [2256] Minimum Average Difference

# @lc code=start

# Approach: Using prefix sum
# Time: O(n) , Space: O(n)

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        count = 1
        n = len(nums)
        avg_diff = dict()

        for i, num in enumerate(nums):
            left_sum += num
            right_sum = total_sum - left_sum
            if n-count > 0:
                result = left_sum//count - right_sum//(n-count)
                avg_diff[i] = abs(result)
            else:
                result = left_sum//count
                avg_diff[i] = abs(result)
            count += 1
        # return min(values, key= lambda x: values[x])
        return min(avg_diff, key=avg_diff.get)

# @lc code=end
