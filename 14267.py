import sys
sys.setrecursionlimit(10**6)
from sys import stdin as s
s = open("input.txt", "r")
n, m = map(int, s.readline().split())
superior_list = list(map(int, s.readline().split()))

graph = {} # key: 직원번호, value: 직속 부하 리스트
for i, superior in enumerate(superior_list):
    if superior == -1: continue
    staff = i + 1
    graph.setdefault(superior, [])
    graph[superior].append(staff)

praise = {}
for _ in range(m):
    staff, w = map(int, s.readline().split())
    praise[staff] = praise.get(staff, 0) + w

score_list = [0] * (n+1)
def dfs(node, score):
    global praise, score_list
    score = score + praise.get(node, 0)
    score_list[node] += score
    for next_node in graph.get(node, []):
        dfs(next_node, score)

dfs(1, 0)
print(' '.join(map(str, score_list[1:])))