#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# Approach: Floyd’s Tortoise & Hare algo, two pointers one twice as fast than slow and one slow
# Time: O(n) , Space: O(1)

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # if fast pointer catch up to slow in a loop, since its twice as fast than slow
            if fast == slow:
                return True
        return False


# Approach: Using a hashmap or hashset storing node objects & frequencies, if the node is already in hashmap, its been encountered again
# Time: O(n) , Space: O(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        values = {}
        while head:
            # check if node object is already there in hashmap, means visited before
            if values.get(head):
                return True
            values[head] = 1
            head = head.next
        return False
        
# @lc code=end

