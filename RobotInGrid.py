#!/usr/local/bin/python3.7

"""Robot In A Grid

"""
from typing import Set, List, Tuple

def findPath(r, c: int, offlimit: Set) -> List[Tuple[int, int]]:
    def step(x, y: int, path) -> List[Tuple[int, int]]:
        if (x > r) or (y > c):
            return None
        elif (x, y) in offlimit:
            return None

        path.append((x,y)) 

        if (x == r) and (y == c):
            return path

        newpath = step(x+1,y, path)
        if newpath:
            return newpath

        newpath = step(x,y+1, path)
        if newpath:
            return newpath

        return None

    path = []

    return step(0,0, path)


r = 4
c = 4
offlimit = set([(1,0), (1,2), (2,1)])

print(findPath(r,c,offlimit))