#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
# Approach: Floyd’s Tortoise & Hare algo, two pointers one fast twice as fast of slow pointer will eventually catch up to slow pointer in a loop
# Time: O(n) , Space: O(1) -> constant memory

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break

        # initiate a new slow pointer from head, as cycle exist so now to check distance covered between head to the start of the cycle with distance covered between point of contact to the start of cycle, since both the distance will be same, we will find the start of cycle
        slow_new = head
        while slow_new and slow:
            if slow == slow_new:
                return slow
            slow = slow.next
            slow_new = slow_new.next
        return
    

# Approach: Using a hashmap or hashset storing node object and their frequencies, if the node is already in hashmap, its been encountered again.
# Time: O(n) , Space: O(n)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        lookup = set()
        while head:
            if head in lookup: return head
            lookup.add(head)
            head = head.next
        return None
        
# @lc code=end

