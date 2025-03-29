from itertools import combinations
from sys import stdin as s
s = open("input.txt", "rt")

N, S = map(int, s.readline().split())
nums = list(map(int, s.readline().split()))

answer = 0
for select in range(1, N+1):
    for candidate in combinations(nums, select):
        if sum(candidate) == S:
            answer += 1

print(answer)