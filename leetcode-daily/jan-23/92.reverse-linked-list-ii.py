# @before-stub-for-debug-begin
from python3problem92 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# *Approach: Reversing the list from left to right using two pointers while storing pointer to previous to the "left" node
# *Time: O(n) , Space: O(1)

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # Phase 1: reach node at position "left"
        left_prev, curr = dummy, head
        for i in range(left - 1):
            left_prev, curr = curr, curr.next

        # now: curr is "left", left_prev is node before "left"
        # Phase 2: Reverse the linked list from position left to right
        prev = None
        for i in range(right - left + 1):
            temp_next = curr.next
            curr.next = prev
            prev, curr = curr, temp_next

        # Phase 3: Update pointers
        left_prev.next.next = curr  # curr is node after "right"
        left_prev.next = prev  # prev is "righ
        return dummy.next
        
# @lc code=end

