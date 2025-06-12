import sys
sys.setrecursionlimit(10**6)
from sys import stdin as s
s = open("input.txt", "r")
nums = [int(row.strip()) for row in s.readlines()]

def recursive(nums):
    if len(nums) <= 1: return nums

    root = nums[0]
    left, right = [], []
    for num in nums[1:]:
        if num < root:
            left.append(num)
        else:
            right.append(num)
    
    result = recursive(left) + recursive(right) + [root]
    return result

print('\n'.join(map(str, recursive(nums))))