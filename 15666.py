from itertools import combinations_with_replacement
from sys import stdin as s
s = open("input.txt", "r")

N, M = map(int, s.readline().split())
nums = list(map(int, s.readline().split()))

nums = sorted(nums)
answers = sorted(list(set(combinations_with_replacement(nums, M))))
for answer in answers :
    print(' '.join(map(str, answer)))