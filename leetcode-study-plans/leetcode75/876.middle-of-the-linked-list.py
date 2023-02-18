#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#
# Approach: Tortoise and Hare approach, two pointers one fast and one slow
# Time: O(n/2)-> O(n) (traversing half elements since fast pointer speed is twice that of slow)
# Space: O(1)

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
# @lc code=end

