from collections import deque
from sys import stdin as s
s = open("input.txt", "r")
N, K = map(int, s.readline().split())

# BFS
q = deque([(N, 0)])
visited = {N: True}
while q:
    position, step = q.popleft()
    if position == K: break
    
    for next_position in [position*2, position+1, position-1]:
        if 0 <= next_position <= 100000 and visited.get(next_position) is None:
            q.append((next_position, step+1))
            visited[next_position] = True

print(step)