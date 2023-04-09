# Implement a string repeater in O(logn) time complexity that repeats a given string 's' by 'n' number of times
def string_repeater(s, n):
    if n == 0:
        return ''
    result = ''
    while n > 0:
        if n % 2 == 1:
            result += s
        s += s
        n //= 2
    return result


# example usage
s = 'hello'
n = 5
print(string_repeater(s, n))


# using recursion
def string_repeater(s, n):
    if n == 0:
        return ''
    if n % 2 == 0:
        half = string_repeater(s, n // 2)
        return half + half
    else:
        return s + string_repeater(s, n - 1)


# example usage
s = 'hello'
n = 5
print(string_repeater(s, n))
