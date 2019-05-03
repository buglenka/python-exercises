#!/usr/local/bin/python3.7

"""Image Overlap
Two images A and B are given, represented as binary, square 
matrices of the same size.  (A binary matrix has only 0s and 1s as 
values.)

We translate one image however we choose (sliding it left, right, up, 
or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
Notes: 

1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1
"""

from typing import List
from collections import defaultdict

def sum1(A: List[List[int]], B: List[List[int]], 
                        bound1: int, bound2: int, maxbound: int) -> int:
    sum = 0
    for rx, ry in zip(A[:maxbound-bound2], B[bound2:]):
        for x, y in zip(rx[:maxbound-bound1], ry[bound1:]):
            if x == y == 1:
                sum += 1

    return sum

def right_down_sums(A: List[List[int]], B: List[List[int]]) -> int:
    size = len(A)
    max_sum = 0

    for dir1 in range(size):
        sum = 0
        for dir2 in range(size):
            if dir1 == dir2 == 0:
                continue

            # count sum for this position
            max_sum = max(max_sum, sum1(A, B, dir1, dir2, size))

    return max_sum

def largestOverlap(A: List[List[int]], B: List[List[int]]) -> int:
    # There are 5 cases with sliding A over B.

    # 1. Translation A to right and down
    max_sum = right_down_sums(A, B)

    # 2. Translation A to left and up
    max_sum = max(max_sum, right_down_sums(B, A))

    # 3. Translation A to right and up
    max_sum = max(max_sum, right_down_sums(A[::-1], B[::-1]))

    # 4. Translation A to left and down
    max_sum = max(max_sum, right_down_sums(B[::-1], A[::-1]))
        
    # 5. Without translation
    sum = 0
    for rx, ry in zip(A, B):
        for x, y in zip(rx, ry):
            if x == y == 1:
                sum += 1

    max_sum = max(max_sum, sum)

    return max_sum

def largestOverlap2(A: List[List[int]], B: List[List[int]]) -> int:
        l = len(A)
        MULT = 100
        
        # Difference bitween coordinates is the number of slidings
        a = [i//l*MULT + i%l for i in range(l*l) if A[i//l][i%l] == 1]
        b = [i//l*MULT + i%l for i in range(l*l) if B[i//l][i%l] == 1]
        
        sm = defaultdict(int)
        
        for i in a:
            for j in b:
                sm[i - j] += 1  
        
        return max(sm.values() or [0])

A = [[0,0,0,1],[1,1,1,0],[0,0,0,1],[0,1,0,0]]
B = [[0,0,0,1],[0,0,0,1],[0,0,1,0],[0,0,0,0]]

print(largestOverlap(A, B))
print(largestOverlap2(A, B))