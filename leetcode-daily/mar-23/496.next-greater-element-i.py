#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#


# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        # optimization to not go through the entire nums2 array
        indices = {}
        for i in range(len(nums2)):
            indices[nums2[i]] = i

        for i in range(len(nums1)):
            for j in range(indices[nums1[i]], len(nums2)):
                if nums2[j] > nums1[i]:
                    ans.append(nums2[j])
                    break
            else:
                ans.append(-1)
        return ans


# @lc code=end
