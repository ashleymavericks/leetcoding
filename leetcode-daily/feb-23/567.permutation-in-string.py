# @before-stub-for-debug-begin
from python3problem567 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# Approach: Hashmap / Array + Sliding windows
# Time: O(n) , Space: O(2*26)

# @lc code=start

# Using Hashmap + Sliding Window
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)

        if len1 > len2:
            return False

        # dict(zip(string.ascii_lowercase, [0]*26))  -> another approach for creating this dict
        dict1 = dict.fromkeys(string.ascii_lowercase, 0)
        dict2 = dict.fromkeys(string.ascii_lowercase, 0)

        for i in range(len1):
            dict1[s1[i]] += 1
            dict2[s2[i]] += 1

        for i in range(len2-len1):
            if dict1 == dict2:
                return True

            dict2[s2[i]] -= 1
            dict2[s2[i+len1]] += 1

        return dict1 == dict2
    

# Using Array + Sliding Window
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)

        if len1 > len2:
            return False

        countS1, countS2 = [0]*26, [0]*26

        for i in range(len1):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1

        for i in range(len2-len1):
            if countS1 == countS2:
                return True

            countS2[ord(s2[i]) - ord('a')] -= 1
            countS2[ord(s2[i+len1]) - ord('a')] += 1

        return countS1 == countS2
      
# @lc code=end

