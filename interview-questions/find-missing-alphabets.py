"""
Given a sting find all the missing alphabets in it.
Input: 'A quick brown fox jumps over the little lazy poo'
Output: ['d','g']
"""
# *Time: O(n) -> where n is the length of the input string
# *Space: O(26) -> Constant memory -> because the size of the frequency array and the size of the res list do not depend on the size of the input string

def find_alphabets(string):
    frequency = [0]*26
    res = []
    for i in string.lower():
        position = ord(i) - ord('a')
        if position < len(frequency) and position >= 0:
            frequency[position] += 1
    for i in range(len(frequency)):
        if frequency[i] == 0:
            res.append(chr(ord('a')+ i))
    return res
            
print(find_alphabets('A quick brown fox jumps over the little lazy poo'))
