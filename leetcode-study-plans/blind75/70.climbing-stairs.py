#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# Approach: Bottom-up Dynamic Programming
# Time: O(n) , Space: O(1)

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one


# Approach: Mathematical approach based on the Fibonacci sequence.
# Time: O() , Space: O()
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n
        first_step = 1
        second_step = 2
        for i in range(3, n+1):
            third_step = first_step + second_step
            first_step = second_step
            second_step = third_step
        return second_step
        
# @lc code=end

