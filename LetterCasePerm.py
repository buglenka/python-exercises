#!/usr/local/bin/python3.7

"""Letter Case Permutation

Given a string S, we can transform every letter individually 
to be lowercase or uppercase to create another string.  
Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""
import string
from typing import List

def letterCasePermutation(S: str) -> List[str]:
    parts = []
    
    part = ''
    for a in S:
        part += a

        if a in string.ascii_letters:
            parts.append([part.lower(), part.upper()])
            part = ''
            
    l = len(parts)
    
    if (part != '') and l > 0:
        parts[-1][0] += part
        parts[-1][1] += part
        
    if (l == 0):
        return [S]
    
    # Join parts
    result = []
    
    for n in range(2**l):
        permutation = ''

        for i in range(l):
            switch = (n & 2 ** i)>>i
            permutation += parts[i][switch]
        
        result.append(permutation)

    return result

S = "a1b2"

for a in letterCasePermutation(S):
    print(a)