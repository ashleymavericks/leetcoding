# Write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f

# a -> b -> c -> d -> e -> f
# reverse_list(a)  # f -> e -> d -> c -> b -> a

# Iterative approach
# n = number of nodes
# Time: O(n)
# Space: O(1)
def reverse_list(head):
    prev = None
    while head is not None:
        # stored the next node
        next = head.next
        # linked head to previous node
        head.next = prev
        # moved the pointers ahead
        prev = head
        head = next
        return prev


# Recursive approach
# Time: O(n)
# Space: O(n) -> linear space due to call stack
def reverse_list(head, prev = None):
    # base case
    if head is None:
        return prev
    
    next = head.next
    head.next = prev
    return reverse_list(next, head)
