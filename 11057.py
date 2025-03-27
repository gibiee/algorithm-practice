from sys import stdin as s
s = open("input.txt", "rt")

N = int(s.readline().strip())

dp = [[0] * 10 for _ in range(N+1)]
# 행 : 맨 뒷자리 숫자
# 열 : 수의 길이

for col in range(1, N+1):
    for row in range(10):
        if col == 1:
            dp[col][row] = 1
        else:
            dp[col][row] = dp[col][row-1] + dp[col-1][row]

print(sum(dp[-1]) % 10007)