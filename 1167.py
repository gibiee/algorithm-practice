import sys
sys.setrecursionlimit(10**6)
from sys import stdin as s
s = open("input.txt", "rt")

V = int(s.readline().strip())

graph = {}
for _ in range(V):
    info = list(map(int, s.readline().split()))
    for i in range(1, len(info), 2):
        if info[i] == -1: break
        graph.setdefault(info[0], {})
        graph.setdefault(info[i], {})
        graph[info[0]][info[i]] = info[i+1]
        graph[info[i]][info[0]] = info[i+1]

# 임의 노드 1에서 DFS 탐색
route = [1]
visited = {}
def dfs(route, weight):
    global visited
    # print(route, weight)

    current_node = route[-1]
    visited[current_node] = weight

    for next_node, next_weight in graph[current_node].items():
        if visited.get(next_node) is None :
            route.append(next_node)
            dfs(route, weight + next_weight)
            route.pop()

dfs(route, 0)

# end_node를 구하고 이 노드에서 DFS 탐색
end_node, end_weight = sorted(visited.items(), key=lambda x:x[1], reverse=True)[0]

route = [end_node]
visited = {}
dfs(route, 0)

_, max_weight = sorted(visited.items(), key=lambda x:x[1], reverse=True)[0]
print(max_weight)