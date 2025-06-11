from sys import stdin as s
s = open("input.txt", "r")

N = int(s.readline().strip())

maps = []
for _ in range(N):
    row = list(map(int, s.readline().split()))
    maps.append(row)

# Why?
if maps[-1][-1] == 1:
    print(0)
    exit(0)

pipe = [0, 0, 0, 1] # (y1, x1, y2, x2)
answer = 0

# DFS
def dfs(pipe):
    global answer
    # print(pipe)

    y1, x1, y2, x2 = pipe
    if (y2, x2) == (N-1, N-1):
        answer += 1
        return

    # 파이프가 가로인 경우
    if y1 == y2:
        can_moves = [(0, 1, 0, 1), (0, 1, 1, 1)]
    # 파이프가 세로인 경우
    elif x1 == x2 :
        can_moves = [(1, 0, 1, 0), (1, 0, 1, 1)]
    # 파이프가 대각선인 경우
    else:
        can_moves = [(1, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1)]

    for can_move in can_moves:
        my1, mx1, my2, mx2 = can_move
        if 0 <= y2 + my2 < N and 0 <= x2 + mx2 < N:
            next_pipe = [y1 + my1, x1 + mx1, y2 + my2, x2 + mx2]
            ny1, nx1, ny2, nx2 = next_pipe

            # 파이프가 가로 또는 세로인 경우
            if ny1 == ny2 or nx1 == nx2:
                if maps[ny2][nx2] == 1:
                    continue
            # 파이프가 대각선인 경우
            else:
                if maps[ny2-1][nx2] + maps[ny2][nx2-1] + maps[ny2][nx2] > 0:
                    continue

            dfs(next_pipe)

dfs(pipe)
print(answer)