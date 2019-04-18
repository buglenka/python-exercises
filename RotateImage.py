#!/usr/local/bin/python3.7

"""Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""

from typing import List

input = input2 = [
  [ 1, 2, 3, 4],
  [ 5, 6, 7, 8],
  [ 9,10,11,12],
  [13,14,15,16]

]

def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    l = len(matrix)

    for f in range(l//2): # Frames
        # Make circular transition of each element from 
        # a row inside a frame
        start = f
        end = l - f - 1

        for i in range(l-2*f-1): 
            to_x, to_y = start + i, start
            last_transition_value = matrix[to_x][to_y]

            transitions = [(end, start+i), (end-i, end), (start, end-i)]
            for x, y in transitions:
                matrix[to_x][to_y] = matrix[x][y]
                to_x = x; to_y = y

            matrix[to_x][to_y] = last_transition_value

def rotate2(matrix: List[List[int]]) -> None:
    n = len(matrix)
    a = 0
    b = n-1

    while(a < b):
        for i in range (b - a):
            matrix[a][a+i], matrix[a+i][b] = matrix[a+i][b], matrix[a][a+i]
            matrix[a][a+i], matrix[b][b-i] = matrix[b][b-i], matrix[a][a+i]
            matrix[a][a+i], matrix[b-i][a] = matrix[b-i][a], matrix[a][a+i]
        a += 1
        b -= 1


rotate(input)
rotate2(input2)





