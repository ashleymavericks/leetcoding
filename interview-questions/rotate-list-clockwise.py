"""
Rotate a list clock wise by degree n
"""

def rotate(l, n):
    l1 = [0] * len(l)
    degree = 0
    for i in range(len(l)):
        degree = (i + n) % len(l)
        l1[degree] = l[i]
    return l1


l = [1,2,3,4] 
n = 1 # 0 <= n <= len(l) - 1
print(rotate(l, 2))
