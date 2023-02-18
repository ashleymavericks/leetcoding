# @before-stub-for-debug-begin
from python3problem21 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# Approach: Standard linked list merging pattern
# Time: O(n+m) -> O(n), Space: O(1)

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# To avoid the edge case of an initial no list to add onto, we create a dummy node then we can return dummy.next as our result
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
               tail.next = list1
               list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        # if list1:
        #     tail.next = list1
        # elif list2:
        #     tail.next = list2
        return dummy.next
    
    
# If don't wanna address the edge cases with dummy node, then this approach can be used
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            start = list1
            list1 = list1.next
        else:
            start = list2
            list2 = list2.next

        tail = start
        while list1 and list2:
            if list1.val < list2.val:
               tail.next = list1
               list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 or list2
        # if list1:
        #     tail.next = list1
        # elif list2:
        #     tail.next = list2
        return start
    
# @lc code=end

