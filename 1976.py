import sys
sys.setrecursionlimit(10**6)
from sys import stdin as s
s = open("input.txt", "r")

N = int(s.readline().strip())
M = int(s.readline().strip())

graph = {}
for i in range(N):
    for j, v in enumerate(map(int, s.readline().split())):
        if v == 1 or i == j:
            node1, node2 = i+1, j+1
            graph.setdefault(node1, [])
            graph[node1].append(node2)

target_route = list(map(int, s.readline().split()))
target_idx = 0

# DFS
answer = 'NO'
def dfs(route, visited, target_idx):
    global target_route, answer
    print(route)

    cur_node = route[-1]
    if cur_node == target_route[target_idx]:
        target_idx += 1
        if target_idx >= len(target_route):
            answer = 'YES'
            return
    
    for next_node in graph.get(cur_node, []):
        if target_idx > visited.get(next_node, -1):
            route.append(next_node)
            visited[next_node] = target_idx
            dfs(route, visited, target_idx)
            if answer == 'YES': return

start_node = target_route[0]
dfs([start_node], {start_node: 0}, 0)

print(answer)