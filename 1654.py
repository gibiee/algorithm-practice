from sys import stdin as s
s = open("input.txt", "rt")

K, N = map(int, s.readline().split())
sizes = [int(s.readline().strip()) for _ in range(K)]
sizes

min_size, max_size = 1, max(sizes)
answer = 1
while max_size >= min_size:
    target_size = (min_size + max_size) // 2
    count = sum([size // target_size for size in sizes])
    print(min_size, target_size, max_size, count)

    if count >= N:
        answer = max(answer, target_size)
        min_size = target_size + 1
    else:
        max_size = target_size - 1

print(answer)