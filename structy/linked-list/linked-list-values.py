# Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# Iterative approach
def linked_list_values(head):
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


# Recursive approach
def linked_list_values(head):
    values = []
    fill_values(head, values)
    return values

def fill_values(head, values):
    if head is None:
        return
    values.append(head.val)
    fill_values(head.next, values)
