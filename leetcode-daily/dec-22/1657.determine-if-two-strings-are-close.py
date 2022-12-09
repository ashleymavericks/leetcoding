#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start

# Approach: Leveraging Counter sub-class to generate hashmap and Set
# Time: O(2n) , Space: O(2n)

# Counter is a sub-class of dict() that is used to count hashable objects. It implicitly creates a hash table of an iterable when invoked and result is in descended sorted order of values.

# but we are still using sorted() on counter for values to get a list object (<class 'list'>) instead of a dict object (<class 'dict_values'>)

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        # c1 = {}
        # c2 = {}

        # for i in word1:
        #     if i not in c1:
        #         c1[i] = 1
        #     else:
        #         c1[i] = c1[i] + 1

        # for j in word2:
        #     if c2.get(j) is None:
        #         c2[j] = 1
        #     else:
        #         c2[j] = c2[j] + 1

        c1 = Counter(word1)
        c2 = Counter(word2)

        if sorted(c1.values()) == sorted(c2.values()) and set(word1) == set(word2):
            return True
        else:
            return False
        
# @lc code=end

