a #
# @lc app=leetcode id=2306 lang=python3
#
# [2306] Naming a Company
#
# Approach: Common prefix sets with distinct suffix

# Time: O(n.26^2) -> O(n) [n -> counting suffix exists in both sets, 26^2 -> nested loop] , Space: O()

# @lc code=start
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # map first char -> list of word suffixes
        wordMap = collections.defaultdict(set)
        # defaultdict with a Hashset default value means if we try a to index a key before inserting, it will use like an empty Hashset
        # defaultdict(<class 'set'>, {'c': {'offee'}, 'd': {'onuts'}, 't': {'offee', 'ime'}})
        for w in ideas:
            wordMap[w[0]].add(w[1:])

        res = 0
        for char1 in wordMap:
            for char2 in wordMap:
                if char1 == char2:
                    continue
                intersect = 0
                
                # checking the intersecting suffixes
                intersect = len(wordMap[char1] & wordMap[char2])
                # for w in wordMap[char1]:
                #     if w in wordMap[char2]:
                #         intersect += 1
                
                distinct1 = len(wordMap[char1]) - intersect
                distinct2 = len(wordMap[char2]) - intersect

                # not multiplying by 2 as for loop is considering both cases char1 <-> char2, thus both sets distinct will covered considering order swapping
                res += distinct1 * distinct2
        return res
        
# @lc code=end

