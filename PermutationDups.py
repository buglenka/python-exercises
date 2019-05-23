#!/usr/local/bin/python3.7

"""Permutations

1. Write a method to compute all permutations of a string of unique characters.
2. String has duplicates.
"""
from typing import List
import math

from collections import Counter

def permutations(S: str) -> List[str]:
    if len(S) < 1:
        return []

    current = [S[0]]

    for idx in range(1, len(S)):
        ch = S[idx]
        next = []

        for s in current:
            next.append(s + ch)
            next.append(ch + s)
            for i in range(1, len(s)-1):
                next.append(s[:i] + ch + s[i:])

        current = next

    return current

def permutations2(S: str) -> List[str]:
    if len(S) < 1:
        return []

    c = Counter(S)
    SS = ''.join(map(lambda x: x[0]*x[1], 
                        c.most_common()[::-1]))

    current = [SS[0]]

    for idx in range(1, len(SS)):
        ch = SS[idx]
        next = set()

        for s in current:
            next.add(s + ch)
            next.add(ch + s)
            for i in range(1, len(s)-1):
                next.add(s[:i] + ch + s[i:])

        current = next

    return current

                 
a = 'abcd'
print(permutations(a))
a = 'abad'
print(permutations2(a))