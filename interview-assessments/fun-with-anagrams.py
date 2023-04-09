"""
Find anagrams in list of stings and return a sorted list post removing the anagram copy.
"""

def funWithAnagrams(text):
    result = []
    anagrams = set()
    for string in text:
        sorted_string = tuple(sorted(string))
        if sorted_string not in anagrams:
            anagrams.add(sorted_string)
            result.append(string)
    return sorted(result)


text = ['code', 'doce', 'ecod', 'framer', 'frame']
result = funWithAnagrams(text)
print(list(result))
