# Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

# Do this in-place, by mutating the original Nodes. You may assume that both input lists are non-empty.

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# a = Node("a")
# b = Node("b")
# c = Node("c")
# a.next = b
# b.next = c
# a -> b -> c

# x = Node("x")
# y = Node("y")
# z = Node("z")
# x.next = y
# y.next = z
# x -> y -> z

# a -> x -> b -> y -> c -> z -> d -> e -> f

## Iterative approach - 1 (Standard pattern)
# n = length of list 1
# m = length of list 2
# Time: O(min(n, m))
# Space: O(1)
def zipper_lists(head_1, head_2):
    tail = head_1
    current_1 = head_1.next
    current_2 = head_2
    count = 0
    while current_1 is not None and current_2 is not None:
        if count % 2 == 0:
            tail.next = current_2
            current_2 = current_2.next
        else:
            tail.next = current_1
            current_1 = current_1.next
        tail = tail.next
        count += 1
    # if one of lists ends early / shorter than others, tackle remaining elements
    if current_1 is not None:
        tail.next = current_1
    if current_2 is not None:
        tail.next = current_2
    return head_1


## Iterative approach - 2 (just worked is this Zippered case due to constant switching of both the lists)
def zipper_lists(head_1, head_2):
    if head_1 is None:
        return head_2

    start = head_1
    while head_1 is not None and head_2 is not None:
        next1 = head_1.next
        next2 = head_2.next

        head_1.next = head_2
        head_1 = next1
        # if head_1 is none, we have already pointed its next to head_2 satisfying our solution
        if head_1 is not None:
            head_2.next = head_1
            head_2 = next2
    return start


## Recursive approach
# Time: O(min(n, m))
# Space: O(min(n, m))
def zipper_lists(head_1, head_2):
    # base cases
    if head_1 is None and head_2 is None:
        return None
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1

    next_1 = head_1.next
    next_2 = head_2.next
    head_1.next = head_2
    head_2.next = zipper_lists(next_1, next_2)
    return head_1
