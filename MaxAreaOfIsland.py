#!/usr/local/bin/python3.7

"""Max Area of Island

Given a non-empty 2D array grid of 0's and 1's, an island is a 
group of 1's (representing land) connected 4-directionally 
(horizontal or vertical.) You may assume all four edges of 
the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. 
(If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, 
because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not 
exceed 50.
"""

from typing import List

def addNeighbours(i,j,m,n: int, to_check: List) -> None:
    neighbours = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    for it, jt in neighbours:
        i_, j_ = i+it, j+jt

        if (i_ < 0) or (i_ >= n) or \
            (j_ < 0) or (j_ >= m):
            continue

        to_check.append((i_, j_))
    
    
def maxAreaOfIsland(grid: List[List[int]]) -> int:
    m,n = len(grid[0]), len(grid)
    seen = [[0] * m for i in range(n)]
    
    max_island_area = island_area = 0

    for i in range(n):
        for j in range(m):
            if (seen[i][j]):
                continue

            seen[i][j] = 1   
                
            if (grid[i][j] == 1):
                # start an island
                island_area = 1
                
                # check neighbours
                to_check = list()
                
                addNeighbours(i,j,m,n,to_check)
                    
                while(len(to_check) > 0):
                    i_, j_ = to_check.pop()
                    
                    if (seen[i_][j_]):
                        continue

                    seen[i_][j_] = 1

                    if (grid[i_][j_] == 1):
                        island_area += 1
                        
                        addNeighbours(i_,j_,m,n,to_check)

                if (island_area > max_island_area):
                    max_island_area = island_area

    return max_island_area
    
grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

maxarea = maxAreaOfIsland(grid)

print(maxarea)