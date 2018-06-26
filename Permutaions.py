#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Permutations

Given a smaller string s and a bigger string b, design an algorithm to find 
permutations of the shorter string within the longer one. 

Print the location of each permutation.
"""

import collections


def find(big, small):
    result = []

    counter = collections.Counter(small)

    j = 0
    n = len(small)
    mismatch = 0
    for i in range(len(big)):

        counter[big[i]] -= 1
        mismatch += (counter[big[i]] < 0)
        if i >= n-1:

            if not mismatch:
                result.append((j))

            mismatch -= (counter[big[j]] < 0)
            counter[big[j]] += 1
            j += 1

    return result

print find("cabcbcccbaab", "aab")
