from sys import stdin as s
s = open("input.txt", "rt")

N, M = map(int, s.readline().split())
numbers = [int(s.readline().strip()) for _ in range(N)]
numbers = sorted(numbers) # 오름차순으로 정렬

left, right = 0, 0
answer = float('inf')
while left <= right and right < N :
    diff = numbers[right] - numbers[left]
    if diff < M:
        right += 1
    else:
        answer = min(answer, diff)
        left += 1

print(answer)