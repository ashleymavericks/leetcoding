#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#

# @lc code=start

#  In-place approach
class Solution:
    def addToArrayForm(self, num: 'List[int]', k: 'int') -> 'List[int]':
        num.reverse()
        i = 0
        while k:
            digit = k % 10
            if i < len(num):
                num[i] += digit
            else:
                num.append(digit)

            carry = num[i] // 10 # no need of if statement, 2 // 10 = 0
            num[i] = num[i] % 10 # no need of if statement, 2 % 10 = 2, 12 % 10 = 2

            k = k // 10  # chop off k
            k += carry
            i += 1
        return num[::-1]


# Approach: [1,2,0,0] -> "1200" -> 1200 -> add K -> 1234 -> "1234" -> [1,2,3,4]
class Solution:
    def addToArrayForm(self, num: 'List[int]', k: 'int') -> 'List[int]':
        return [int(s) for s in str(int(''.join(str(x) for x in num)) + k)]
        
# @lc code=end

