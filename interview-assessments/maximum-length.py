"""
You are given a string S of length N which consists of lower case English alphabets,

You are given the Q update queries. Each query contains an integer X[i] and a character Y[i]. You have to update the character of the string S at index X[i] to Y[i] that is, set S[X[i]] = Y[i]

After the update of each query, You have to calculate the maximum length of the substring which is present in S and having the same characters. This substring should contain only 1 distinct character.

- F-based indexing is followed.
- The modified string is used in the next query.
- A substring is the sequence of consecutive elements of the string. For example in string "abc" the substrings are as follows:
    - "" empty string
    - "a"
    - "b"
    - "ab"
    - "bc"
    - "abc"
"""