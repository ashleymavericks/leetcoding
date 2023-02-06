# @before-stub-for-debug-begin
from python3problem953 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {order[i]: i for i in range(len(order))}

        for i in range(len(words)-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if order_dict[words[i][j]] < order_dict[words[i+1][j]]:
                    break
                elif order_dict[words[i][j]] > order_dict[words[i+1][j]]:
                    return False
            else:  # If loop breaks, else block won't execute
                if len(words[i]) > len(words[i+1]):
                    return False
        return True
        
# @lc code=end

