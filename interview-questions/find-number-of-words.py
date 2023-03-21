"""
 Given a string find the number of words in that particular string.
 Input: " my    name  is    anurag"
 Output: 4   
"""

s = " my name    is    anurag"

# with python built-ins
print(len(s.split()))

# do it with counter, without using space
def all_words(s):
    length = []
    word = ''
    for i in s:
        if i != ' ':
            word += i
        else:
            if word:
                length.append(word)
                word = ''
    else:
        length.append(word)
    return print(len(length))


all_words(s)

