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
        last = len(nums1)-1
        m, n = m - 1, n - 1

        # merge in reverse order
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[last] = nums1[m]
                m -= 1
            else:
                nums1[last] = nums2[n]
                n -= 1
            last -= 1

        # fill nums1 with leftover nums2 elements, opposite case won't be possible since final output is in nums1 array
        while n >= 0:
            nums1[last] = nums2[n]
            n, last = n - 1, last - 1

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

