from sys import stdin as s
s = open("input.txt", "r")

N = int(s.readline().strip())

maps = []
for _ in range(N):
    row = list(map(int, s.readline().split()))
    maps.append(row)

dp = [[[0,0,0] for _1 in range(N)] for _2 in range(N)]
# dp[y][x][d] : (y, x) 위치에 파이프가 d 방향으로 올 수 있는 경우의 수
# d = 0 : 가로
# d = 1 : 세로
# d = 2 : 대각선
dp[0][1][0] = 1

for y in range(N):
    for x in range(N):
        if x-1 >= 0 and maps[y][x] != 1:
            dp[y][x][0] += dp[y][x-1][0] + dp[y][x-1][2]
        if y-1 >= 0 and maps[y][x] != 1:
            dp[y][x][1] += dp[y-1][x][1] + dp[y-1][x][2]
        if y-1 >= 0 and x-1 >= 0 and maps[y-1][x] != 1 and maps[y][x-1] != 1 and maps[y][x] != 1:
            dp[y][x][2] += dp[y-1][x-1][0] + dp[y-1][x-1][1] + dp[y-1][x-1][2]

print(sum(dp[-1][-1]))