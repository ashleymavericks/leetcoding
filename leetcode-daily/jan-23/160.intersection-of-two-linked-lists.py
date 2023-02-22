#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#
# Approach: Fine the length of linked-list and increment the head pointer of the longer list with the difference.
# Time: O(m+n) , Space: O(1)

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1 = headA
        l2 = headB

        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1
    
# ====================================================================

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dist1, dist2 = 0, 0
        currA, currB = headA, headB
        # calculating the length of linked-lists
        while currA:
            dist1 += 1
            currA = currA.next
        while currB:
            dist2 += 1
            currB = currB.next
        # If different end points, didn't intersect
        if currA != currB:
            return
        # Increment the head pointer of the longer linked-list
        if dist1 > dist2:
            dist = dist1-dist2
            while dist:
                headA = headA.next
                dist -= 1
        else:
            dist = dist2-dist1
            while dist:
                headB = headB.next
                dist -= 1
        # Now so simply iterate & compare to check for intersection
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return


# Approach: Using hashset (extra memory) store entire listA nodes, then compare iteratively with listB to find the intersection point if any
# Time: O(m+n) , Space: O(number of nodes of listA is m) -> O(m)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list1 = set()
        while headA:
            list1.add(headA)
            headA = headA.next

        while headB:
            if headB in list1:
                return headB
            headB = headB.next
        return
        
# @lc code=end

