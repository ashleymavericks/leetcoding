"""
Mathematics: Divisible N-Digit Number

You are given three Integers N, A, and B You need to print the number of positive integers having N digits that are divisible by A or B

Note: N-digit integer is a positive integer containing N digits (0.1,2,3,4,5,6,7,8,9) in its decimal representation.

For example, 4090 is a 4-digit number.

Example:
N=1, A= 4, 8=5
The one-digit numbers divisible by 4 are 4, 8. The one-digit number(s) divisible by 5 is 5.
Hence the answer is 3.

Input Format:
The Input contains three space-separated integers N, A, and B

Sample Input:
1 2 3 - denotes N, A & B separated by a space

Output Format:
The output contains a single integer denoting a positive integer having N digits that are divisible by A or by B

Sample Output:
Considering every N=1
(1,5,7) are neither divisible by 2 nor by 3. 
(2,4,8) are divisible by 2 only
(3,9) are divisible by 3 only
(6) is divisible by both 2 and 3

The single-digit numbers that are completely divisible by 2 or 3 are. (2,3,4,6,8,9)
Hence, the output is 6.
"""

#*  Further optimized approach to reduce even generated values
def Divisibility(N, A, B):
    result = 0

    def gen(N, lcm):
        i = lcm
        while i < 10**N:
            yield i
            i += lcm

    # calculate the LCM of A and B
    def lcm(a, b):
        from math import gcd
        return a * b // gcd(a, b)

    # generate only the multiples of the LCM
    for i in gen(N, lcm(A, B)):
        if i % A == 0 or i % B == 0:
            result += 1

    return result

# INPUT
temp1 = input().split()
N = int(temp1[0])
A = int(temp1[1])
B = int(temp1[2])

# OUTPUT
print(Divisibility(N, A, B))


#* Optimized approach using generators
def Divisibility(N, A, B):
    result = 0

    def gen(N): 
        i = 1
        while i < 10**N:
            yield i
            i += 1

    for i in gen(N):
        if i % A == 0 or i % B == 0:
            result += 1
            
    return result

# INPUT 
temp1 = input().split()
N = int(temp1[0])
A = int(temp1[1])
B = int(temp1[2])

# OUTPUT 
print(Divisibility(N, A, B))