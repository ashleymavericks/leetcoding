# Write a function, linked_list_find, that takes in the head of a linked list and a target value. The function should return a boolean indicating whether or not the linked list contains the target

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# Iterative approach
# n = number of nodes
# Time: O(n)
# Space: O(1)
def linked_list_find(head, target):
    while head is not None:
        if head.val == target:
            return True
        head = head.next
    return False


# Recursive approach
# Time: O(n)
# Space: O(n)
def linked_list_find(head, target):
    if head is None:
        return False
    if head.val == target:
        return True
    return linked_list_find(head.next, target)
