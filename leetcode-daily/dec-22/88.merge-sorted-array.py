#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start

# without using extra space, O(1) -> Space Complexity
        

# using temp table with extra space, O(n) -> Space Complexity
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp, i, j, k = [], 0, 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        while i < m:
            temp.append(nums1[i])
            i+=1
        while j < n:
            temp.append(nums2[j])
            j+=1

        # nums1 = list(temp) -> not sure, why not working on LC
        # nums1 = temp.copy() -> not sure, why not working on LC
        while k < m+n:
            nums1[k] = temp[k]
            k += 1
     
# @lc code=end

