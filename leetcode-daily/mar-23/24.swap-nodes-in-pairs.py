#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# Approach: Keep a dummy node for linked list problems, it helps!
# Time: O(n) , Space: O(1) -> Constant memory

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(next=head)

        while head and head.next:
            second = head.next  # second node of the pair
            prev.next = second
            head.next = head.next.next
            second.next = head

            head = head.next
            prev = prev.next.next

        return dummy.next

        
# @lc code=end

