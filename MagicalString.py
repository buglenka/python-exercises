#!/usr/local/bin/python3.7

"""Magical String

A magical string S consists of only '1' and '2' and obeys the 
following rules:

The string S is magical because concatenating the number of contiguous 
occurrences of characters '1' and '2' generates the string S itself.

The first few elements of string S is the following: 
S = "1221121221221121122……"

If we group the consecutive '1's and '2's in S, it will be:

1 22 11 2 1 22 1 22 11 2 11 22 ......

and the occurrences of '1's or '2's in each group are:

1 2	2 1 1 2 1 2 2 1 2 2 ......

You can see that the occurrence sequence above is the S itself.

Given an integer N as input, return the number of '1's in the first N 
number in the magical string S.

Note: N will not exceed 100,000.

Example 1:
Input: 6
Output: 3
Explanation: The first 6 elements of magical string S is "12211" and it 
contains three 1's, so return 3.
"""

def magicalString(n: int) -> int:
    if (n == 0):
        return 0
    elif (n < 4):
        return 1
    
    magic_string = [1,2,2]
    num = 1; l = 3; count = 0
    
    # Generate string with n elements
    while(l < n):

        # Start of a new magic string
        string = []
        num = 1; l = 0; count = 0

        for i in magic_string:
            string += [num]*i
            
            if num == 1:
                count += i

            num = num ^ 3
            l += i
                
            if l >= n:
                break
            
        magic_string = string
        
        if l >= n:
            break

    if l != n:
        assert l - n == 1, "Wrong string generated"
        
        # The end of the magic string is ..11
        # But one of '1' is redundant
        if magic_string[-1] == 1:
            count -= 1
            
    return count, magic_string

class Solution:

    @classmethod
    def generateString(cls, n):
        magic_string = [1,2,2]
        l = 3; i = 2; num = 1

        while(l < n):
            magic_string += [num] * magic_string[i]
            l += magic_string[i]
            i += 1

            num = num ^ 3

        cls.string = magic_string

    def magicalString(self, n: int) -> int:
        return self.string[:n].count(1)

Solution.generateString(100000)

# Input
n = 11

# Solution 1
print(magicalString(n))

# Solution 2
a = Solution()
print(a.magicalString(n))