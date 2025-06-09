from sys import stdin as s
s = open("input.txt", "rt")

# 벨만 포드
def bellman_ford(start_node):
    global edges, dist
    dist[start_node] = 0

    for i in range(N+1):
        for edge in edges:
            start, end, cost = edge
            if dist[start] != float('inf') and dist[end] > dist[start] + cost:
                dist[end] = dist[start] + cost

                # N 번째 라운드에서도 값이 갱신된다면 음수 순환 존재
                if i == N:
                    return True
    return False

TC = int(s.readline().strip())
for tc in range(TC):
    N, M, W = map(int, s.readline().split())
    edges = []
    for _ in range(M):
        S, E, T = map(int, s.readline().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    
    start_nodes = []
    for _ in range(W):
        S, E, T = map(int, s.readline().split())
        start_nodes.append(S)
        edges.append((S, E, -T))
    
    # 모든 정점과 연결되는 가상 노드 0번 추가
    for node in range(1, N+1):
        edges.append((0, node, 0))

    dist = [float('inf')] * (N+1)
    negative_cycle = bellman_ford(start_node=0)
    print('YES') if negative_cycle else print('NO')