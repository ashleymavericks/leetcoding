"""
Given a binary tree representation in form of list of lists where 1st element in lists are the parent nodes and 1st element in first list is the root node, find its leaf nodes.

tree = [
    [1,2,3],
    [2,4,5]
    [3,6,7]
    [4,8,9]
    [5,10,11]
    [6,12,13]
    [7,14,15]
]

output = [8, 9, 10, 11, 12, 13, 14, 15]
"""
# leaf nodes frequency will be 1, can leverage that to solve this problem