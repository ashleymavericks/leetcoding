# @before-stub-for-debug-begin
from python3problem328 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#
# Approach 1: Traverse the linked list once and at the same time segregate both odd and even nodes, at the end connect the odd nodes end to even node start.
# Time: O(nodes)->O(n) , Space: O(1)

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return

        odd_head, odd = head, head
        even_head, even = head.next, head.next

        while odd and odd.next and even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        # tail of odd_head i.e. odd to even head
        odd.next = even_head
        return odd_head
    
    
# Approach 2: In first iteration will get the count of the jumps needed for this the given list, basically the length of the list, even or odd, then in next iteration we perform a 3 part operation to add even elements at the end.
# Time: O(nodes)->O(n) , Space: O(1)

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count, temp, end = 0, head, head

	# boundary case
        if not head:
            return

        while end and end.next:
            count += 1
            end = end.next

        # for even count value (hops needed) // 2 (total nodes are odd)
        # for odd count value (hops needed) // 2 + 1 (total nodes are even)
        count = (count // 2) + 1 if count % 2 else count // 2
        while count:
            end.next = temp.next
            temp.next = temp.next.next
            end.next.next = None
            temp = temp.next
            end = end.next
            count -= 1
        return head
    
# @lc code=end

