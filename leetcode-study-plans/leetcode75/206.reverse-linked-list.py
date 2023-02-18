#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach: Two pointers
# Time: O(n) , Space: O(1) -> constant space
# Iterative appraoch
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
		# stored the next node
            next = head.next
	# linked head to previous node
            head.next = prev
	# moved the pointers ahead
            prev = head
            head = next
        return prev


# Time: O(n) , Space: O(n) -> linear space due to call stack
# Recursive approach
class Solution:
    def reverseList(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:
	# base case
        if head is None:
            return prev

        next = head.next
        head.next = prev
        return self.reverseList(next, head)  # return prev to all the way back
    
        
# @lc code=end

