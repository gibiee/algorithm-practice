from collections import deque
from sys import stdin as s
s = open("input.txt", "rt")

case_idx = 1
while True:
    n, m = map(int, s.readline().split())
    if (n, m) == (0,0): break

    graph = {i: [] for i in range(1, n+1)}
    for _ in range(m):
        a, b = map(int, s.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    answer = 0
    visited = {}
    for start_node in range(1, n+1):
        if visited.get(start_node) is not None: continue

        route = deque([start_node])
        visited[start_node] = 'start'
        status = 'tree'
        while route:
            # print(route)
            current_node = route.popleft()
            for next_node in graph[current_node]:
                if visited.get(next_node) is None:
                    route.append(next_node)
                    visited[next_node] = current_node
                elif next_node == visited[current_node]:
                    continue
                else:
                    status = 'not tree'
            
        if status == 'tree': answer += 1

    if answer == 0:
        print(f"Case {case_idx}: No trees.")
    elif answer == 1:
        print(f"Case {case_idx}: There is one tree.")
    else:
        print(f"Case {case_idx}: A forest of {answer} trees.")

    case_idx += 1