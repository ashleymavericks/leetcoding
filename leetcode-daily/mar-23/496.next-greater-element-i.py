#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
# Approach: Monotonic stack -> finding a lot of next greater element at one go
# Time: O(n) -> O(nums1.length + nums2.length) , Space: O(nums1) -> hashmap and stach both will be of the size of first array

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indices = {n: i for i, n in enumerate(nums1)}
        arr = [-1] * len(nums1)
        stack = []

        for i in nums2:
            while stack and i > stack[-1]:
                popped = stack.pop()
                arr[indices[popped]] = i
            if i in indices:
                stack.append(i)

        return arr
    
    
# Approach: Create an indices hashmap for nums2 so that we don't have to traverse the whole array
# Time: O(n^2) -> O(m.n)  , Space: O(nums1)
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
