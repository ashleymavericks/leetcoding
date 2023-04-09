"""
Reverse a string but recursively!
"""

def reverse_string(s):
    # base case
    if len(s) == 0:
        return s
    # recursive case
    else:
        return reverse_string(s[1:]) + s[0]


# example usage
s = "hello world"
print(reverse_string(s))
