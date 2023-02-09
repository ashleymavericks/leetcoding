# @before-stub-for-debug-begin
from python3problem904 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start

# find the longest continuous sub array that has exactly 2 distinct elements
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Both below solves the key not found error issue
        # count = collections.defaultdict(int) 
        # count = collections.Counter()
        count = dict()
        l, total, res = 0, 0, 0

        for r in range(len(fruits)):
            # count[fruits[r]] += 1
            if count.get(fruits[r]):
                count[fruits[r]] += 1
            else:
                count[fruits[r]] = 1
            total += 1

            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1
                total -= 1
                l += 1
                if not count[f]:
                    count.pop(f)

            res = max(total, res)
        return res
    
# A slightly different way to iterate the sliding window across the array
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_count, curr_count, j, i = 0, 0, 0, 0
        unique = {}
        while i < len(fruits) and j < len(fruits):
            if unique.get(fruits[j]):
                unique[fruits[j]] += 1
            else:
                unique[fruits[j]] = 1
            j += 1
            curr_count += 1

            if len(unique) > 2:
                f = fruits[i]
                unique[f] -= 1
                curr_count -= 1
                if not unique[f]:
                    unique.pop(f)
                i += 1
            max_count = max(curr_count, max_count)
        return max_count

# @lc code=end
