from sys import stdin as s
s = open("input.txt", "rt")

N, S = map(int, s.readline().split())
numbers = list(map(int, s.readline().split()))

left, right = 0, 0
total = numbers[left]
answer = float('inf')
while left <= right and right < N:
    if total >= S:
        answer = min(answer, right - left + 1)
        if answer == 1: break
        total = total - numbers[left]
        left += 1
    else:
        right += 1
        if right >= N: break
        total = total + numbers[right]

print(answer) if not answer == float('inf') else print(0)