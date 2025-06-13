from collections import deque
from sys import stdin as s
s = open("input.txt", "r")
N, K = map(int, s.readline().split())

answer_count = 0

# BFS
q = deque([(N, 0)])
visited = {N: 0}
while q:
    position, step = q.popleft()
    if position == K:
        answer_count += 1
        continue
    
    next_step = step + 1
    for next_position in [position*2, position+1, position-1]:
        if 0 <= next_position <= 100000 and next_step <= visited.get(next_position, float('inf')):
            q.append((next_position, next_step))
            visited[next_position] = next_step

print(visited[K])
print(answer_count)