#!/usr/local/bin/python3.7

"""Palindromic Substrings

Given a string, your task is to count how many palindromic 
substrings in this string.

The substrings with different start indexes or end indexes 
are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.
"""

def countSubstrings(s: str) -> int:
    s_extended = '@#' + '#'.join(s) + '#$'
    counters = [0] * len(s_extended)

    # === Manacher's Algorithm ===
    # i - center position
    # Current large polindrome:
    #   c - center position
    #   r - the next index after the right boundary
    #   i_mirror - mirror position if i
    # ============================ 
    c = 0; r = 0
    
    for i in range(1, len(s_extended) - 1):
        i_mirror = 2 * c - i

        if i < r:
            counters[i] = min(counters[i_mirror], r - i)

        while(s_extended[i + counters[i] + 1] == s_extended[i - (counters[i] + 1)]):
            counters[i] += 1
            
        if (i + counters[i] > r):
            r = i + counters[i]
            c = i
    
    return sum((cnt + 1)//2 for cnt in counters)

s = 'aaa'
print(countSubstrings(s))

        
        

