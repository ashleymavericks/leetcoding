#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1, map2 = {}, {}

        # for c1,c2 in zip(s,t):
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            # to check if the key is there and if its already mapped to some different value
            if (c1 in map1 and map1[c1] != c2) or (c2 in map2 and map2[c2] != c1):
                return False
            map1[c1] = c2
            map2[c2] = c1
        return True
        
# @lc code=end

