import heapq
from sys import stdin as s
s = open("input.txt", "rt")

N, M = map(int, s.readline().split())

graph = {}
for _ in range(M):
    A, B, C = map(int, s.readline().split())
    graph.setdefault(A, {})
    graph.setdefault(B, {})
    graph[A][B], graph[B][A] = C, C

# 모든 노드를 연결할 수 있는 최소신장트리 탐색 : 프림 알고리즘
# 시작 가중치 : 0 / 시작 노드 : 1번
heap = [(0, 1)]
heapq.heapify(heap)

visited = {}
while len(heap) > 0:
    weight, node = heapq.heappop(heap)
    if visited.get(node) is not None: continue

    visited[node] = weight
    # print(f"node : {node}, weight : {weight}")

    for next_node, next_weight in graph[node].items():
        if visited.get(next_node) is None:
            # print(f"next_node : {next_node}, next_weight: {next_weight}")
            heapq.heappush(heap, (next_weight, next_node))

weight_list = visited.values()
print(sum(weight_list) - max(weight_list))