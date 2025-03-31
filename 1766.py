import heapq
from sys import stdin as s
s = open("input.txt", "rt")

N, M = map(int, s.readline().split())

graph = {}
degree_list = [0] * (N+1) # 진입 차수
for _ in range(M):
    A, B = map(int, s.readline().split())
    graph.setdefault(A, [])
    graph[A].append(B)
    degree_list[B] += 1

# 진입 차수가 0인 문제들을 쉬운 순서대로 우선순위 큐에 추가
pq = []
for i in range(1, N+1):
    if degree_list[i] == 0:
        heapq.heappush(pq, i)

# 우선순위 큐에서 문제를 빼면서 진입 차수가 0이 된 문제들을 추가
answer = []
while len(pq) > 0:
    question = heapq.heappop(pq)
    answer.append(str(question))
    for next_q in graph.get(question, []):
        degree_list[next_q] -= 1
        if degree_list[next_q] == 0:
            heapq.heappush(pq, next_q)

print(' '.join(answer))