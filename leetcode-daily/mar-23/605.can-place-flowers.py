#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#
# Approach: Similar approach, but with constant memory, keep counting empty space until the next flower is visited and then substract 1 from n for each three contiguous empty spaces
# Time: O(n) , Space: O(1) -> constant memory

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty = 0 if flowerbed[0] else 1
        for f in flowerbed:
            if f:
                # int division, round to zero: -0.5 -> 0
                n -= int((empty - 1)/2)
                empty = 0
            else:
                empty += 1

         # if the last flower is empty, empty value didn't get accounted for, mostly it will matter when last two flower is empty
        n -= empty // 2

        return n <= 0
    
    
# Approach: Modify the initial flowerbed array and add extra flowerbed spaces on both start and the end of the array
# Time: O(n) , Space: O(n)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]  # extra flowerbed space to cover edge cases

        for i in range(1, len(f)-1):  # skip the extra flowerbed positions
            if f[i - 1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i] = 1
                n -= 1
        return n < 1  # n <= 0

# @lc code=end
