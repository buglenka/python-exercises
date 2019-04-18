#!/usr/local/bin/python3.7

"""Trapping Rain Water

Given n non-negative integers representing an elevation map where 
the width of each bar is 1, compute how much water it is able to 
trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
from typing import List

def measure(height: List[int], 
    idx: int, maxHeight: int, border: bool, backward: bool) -> int:
    
    maxidx = 0
    watersum = 0        
    localMaxHeight = 0
    startIdx, endIdx, step = idx, len(height), 1
    
    if not border:
        localMaxHeight = maxHeight
        
    if backward:
        startIdx, endIdx, step = idx, 0, -1
        
    for i in range(startIdx, endIdx, step):
        h = height[i]
        
        if h == maxHeight:
            maxidx = i
            break
            
        if (h > localMaxHeight):
            localMaxHeight = h

        if (h < localMaxHeight):
            watersum += localMaxHeight - h
            
    return maxidx, watersum
    
def trap(height: List[int]) -> int:
    # Find the max heights
    maxHeight = 0
    for i in height:
        if i > maxHeight:
            maxHeight = i
            
    # Calculate the squares with water
    totalSum = 0
    
    # Move forward to Max Height
    fmaxidx, summ = measure(height, 0, 
                                    maxHeight, True, False)
    totalSum += summ
        
    # Move backward to Max Height
    bmaxidx, summ = measure(height, len(height)-1, 
                                    maxHeight, True, True)
    totalSum += summ 
                            
    # Check if there are more than one max height 
    while (fmaxidx != bmaxidx):
        fmaxidx += 1

        fmaxidx, summ = measure(height, fmaxidx, 
                                    maxHeight, False, False)
        totalSum += summ 
    
    return totalSum

map = [0,1,0,2,1,0,1,3,2,1,2,1]

water = trap(map)

print(water)

                
                    
                