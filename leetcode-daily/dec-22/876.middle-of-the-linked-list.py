#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start

# Approach: Leverage two pointers a fast moving one and a slow moving one
# Time: O(n/2) , Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        # while fast is not None and fast.next is not None:
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

# @lc code=end
