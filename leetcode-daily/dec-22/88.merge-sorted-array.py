#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
# Approach: In-place operation without using extra space using three pointers
# Time: O(n) , Space: O(1) -> constant space as no extra memory defined/needed

# without using extra space, O(1) -> Space Complexity
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m-1, n-1, len(nums1)-1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        # insert the leftover elements of another array whose index is not yet gone out of bounds (-1), means it hasn't cover the 0th index element yet
        while i > -1:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        while j > -1:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

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

