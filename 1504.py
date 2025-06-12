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
    
        for next_node, _dist in graph.get(node, []):
            next_dist = dist + _dist
            if distance[next_node] > next_dist:
                distance[next_node] = next_dist
                heapq.heappush(hq, (next_dist, next_node))

    return distance

distance0 = dijkstra(1)
distance1 = dijkstra(V1)
distance2 = dijkstra(V2)
answer1 = distance0[V1] + distance1[V2] + distance2[-1]
answer2 = distance0[V2] + distance2[V1] + distance1[-1]
answer = min(answer1, answer2)
print(answer) if answer is not float('inf') else print(-1)