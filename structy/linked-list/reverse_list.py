# Reverse a singly linked list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

# Iterative approach
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
def reverse_list(head, prev=None):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverse_list(next, head)
