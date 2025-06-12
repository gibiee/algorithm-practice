import heapq
from sys import stdin as s
s = open("input.txt", "r")

N, E = map(int, s.readline().split())
graph = {}
for _ in range(E):
    a, b, c = map(int, s.readline().split())
    graph.setdefault(a, [])
    graph.setdefault(b, [])
    graph[a].append((b,c))
    graph[b].append((a,c))

V1, V2 = map(int, s.readline().split())
def dijkstra(start_node):
    distance = [float('inf')] * (N+1)
    distance[start_node] = 0
    hq = [(0, start_node)] # 현재 이동거리, 현재 노드
    while hq:
        dist, node = heapq.heappop(hq)
        if distance[node] < dist: continue
    
        for next_node, _dist in graph[node]:
            next_dist = dist + _dist
            if distance[next_node] > next_dist:
                distance[next_node] = next_dist
                heapq.heappush(hq, (next_dist, next_node))

    return distance

distance1 = dijkstra(1)
distance2 = dijkstra(V1)
distance3 = dijkstra(V2)
print(distance1[V1] + distance2[V2] + distance3[-1])