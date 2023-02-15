# @before-stub-for-debug-begin
from python3problem438 import *
from typing import *
import collections
# @before-stub-for-debug-end

#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start

# without using collections module
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        sCount, pCount = {}, {}
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)  # to overcome key not found
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        res = [0] if sCount == pCount else []
        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if sCount == pCount:
                res.append(l)
        return res

# using collections.Counter()
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        output, j = [], len(p)-1
        str1 = collections.Counter(s[:j+1])
        str2 = collections.Counter(p)

        for i in range(len(s)-len(p)+1):
            if str1 == str2:
                output.append(i)
                
            str1[s[i]] -= 1  # possible with < class 'collections.Counter' >
            # if str1[s[i]] < 2:
            #     str1.pop(s[i])
            # else:
            #     str1[s[i]] -= 1

            if j < len(s) - 1:
                j += 1
                str1[s[j]] += 1
        return output
        
# @lc code=end

