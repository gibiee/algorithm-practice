import heapq
from sys import stdin as s
s = open("input.txt", "rt")

N, M, X = map(int, s.readline().split())
graph, graph_reversed = {}, {}
for _ in range(M):
    A, B, T = map(int, s.readline().split())
    graph.setdefault(A, [])
    graph_reversed.setdefault(B, [])
    graph[A].append((B, T))
    graph_reversed[B].append((A, T))

def dijkstra(graph, start_node):
    dp = [float('inf')] * (N+1)
    heap = [(0, start_node)] # (이동거리, 다음노드)

    dp[start_node] = 0
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        for able_node, able_distacnce in graph.get(current_node, []):
            next_distacnce = current_distance + able_distacnce
            if next_distacnce < dp[able_node]:
                dp[able_node] = next_distacnce
                heapq.heappush(heap, (next_distacnce, able_node))
    return dp

# 학생 마을 -> X번 마을
dist1 = dijkstra(graph_reversed, X)

# X번 마을 -> 학생 마을
dist2 = dijkstra(graph, X)

dist = [d1+d2 for d1, d2 in zip(dist1[1:], dist2[1:])] 
print(max(dist))