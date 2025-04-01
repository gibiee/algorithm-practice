from collections import deque
from sys import stdin as s
s = open("input.txt", "rt")

N, M = map(int, s.readline().split())
maps = [list(map(int, s.readline().strip())) for _ in range(N)]

# BFS 탐색
answer = -1
route = deque([(0, 0, True, 1)]) # 위치 Y, X, 벽부수기 가능여부, step 수
visited = {}
while route:
    curY, curX, chance, step = route.popleft()
    if (curY, curX) == (N-1, M-1):
        answer = step
        break
    
    moves = [(-1,0), (0,-1), (0,1), (1,0)]
    next_step = step + 1
    for moveY, moveX in moves:
        nextY, nextX = curY + moveY, curX + moveX    
        if 0 <= nextY < N and 0 <= nextX < M:
            if maps[nextY][nextX] == 0 and visited.get((nextY, nextX, chance), float('inf')) > next_step:
                visited[(nextY, nextX, chance)] = next_step
                route.append((nextY, nextX, chance, next_step))
            
            if maps[nextY][nextX] == 1 and chance and visited.get((nextY, nextX, chance), float('inf')) > next_step:
                visited[(nextY, nextX, chance)] = next_step
                route.append((nextY, nextX, False, next_step))

print(answer)