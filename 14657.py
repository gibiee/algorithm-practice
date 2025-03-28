import sys
sys.setrecursionlimit(10**6)
import math
from sys import stdin as s
s = open("input.txt", "rt")

N, T = map(int, s.readline().split())
graph = {}
for _ in range(N-1):
    A, B, C = map(int, s.readline().split())
    graph.setdefault(A, {})
    graph.setdefault(B, {})
    graph[A][B] = C
    graph[B][A] = C

# 임의의 노드를 시작 노드로 설정하여 dfs 수행 -> end_node를 구함
start_node = list(graph.keys())[0]

max_solved, min_time, end_node = 0, float('inf'), None
def dfs(route, visited, total_time):
    global max_solved, min_time, end_node
    current_node = route[-1]

    if max_solved < len(route):
        max_solved = len(route)
        min_time = total_time
        end_node = current_node
    elif max_solved == len(route) and min_time > total_time:
        min_time = total_time
        end_node = current_node

    for next_node, next_time in graph[current_node].items():
        if visited.get(next_node) is None:
            route.append(next_node)
            visited[next_node] = True
            dfs(route, visited, total_time + next_time)
    
    route.pop()
    visited[current_node] = None

route, visited = [start_node], {start_node: 0}
dfs(route, visited, 0)

# 구한 end_node에서 출발하여 다시 dfs 수행
route, visited = [end_node], {end_node: 0}
max_solved, min_time, end_node = 0, float('inf'), None
dfs(route, visited, 0)

print(math.ceil(min_time / T))