import sys
sys.setrecursionlimit(10**6)
from sys import stdin as s
s = open("input.txt", "r")

N = int(s.readline().strip())

graph = {}
for _ in range(N):
    a, b, c = map(int, s.readline().split())
    graph.setdefault(a, {})
    graph[a].update({'left_child': b, 'right_child': c})

graph

# 중위 순회
route_1 = []
def dfs_1(node):
    global route
    if graph[node]['left_child'] !=  -1:
        dfs_1(graph[node]['left_child'])

    route_1.append(node)

    if graph[node]['right_child'] != -1:
        dfs_1(graph[node]['right_child'])

dfs_1(1)
end_node = route_1[-1]

# 유사 중위 순회
route_2, answer = [], None
def dfs_2(node):
    global route_2, answer
    if answer is not None: return
    
    route_2.append(node)
    
    if graph[node]['left_child'] !=  -1:
        dfs_2(graph[node]['left_child'])
        route_2.append(node)
    
    if graph[node]['right_child'] != -1:
        dfs_2(graph[node]['right_child'])
        route_2.append(node)
    
    if node == end_node:
        answer = len(route_2) - 1
        return

dfs_2(1)
print(answer)