from itertools import combinations
from sys import stdin as s
s = open("input.txt", "rt")

N, S = map(int, s.readline().split())
nums = list(map(int, s.readline().split()))

pivot = len(nums) // 2
left_nums, right_nums = nums[:pivot], nums[pivot:]

left_counter = {}
for select in range(1, len(left_nums)+1):
    for candidate in combinations(left_nums, select):
        total = sum(candidate)
        left_counter[total] = left_counter.get(total, 0) + 1

answer = left_counter.get(S, 0)

for select in range(1, len(right_nums)+1):
    for candidate in combinations(right_nums, select):
        total = sum(candidate)
        if total == S: answer += 1
        answer += left_counter.get(S - total, 0)

print(answer)