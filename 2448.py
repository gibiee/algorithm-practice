from sys import stdin as s
s = open("input.txt", "r")

N = int(s.readline().strip())

def recursive(n):
    if n == 3:
        return ["*", "* *", "*****"]
    else:
        top = recursive(n//2)
        left = recursive(n//2)
        mid = [row.replace('*', ' ') for row in reversed(left)]
        right = recursive(n//2)

        result = top
        for p2, p3, p4 in zip(left, mid, right):
            result.append(p2 + p3 + p4)

    return result

answer = recursive(N)
counts = [len(row) for row in answer]
max_count = max(counts)

for row in answer:
    side_space = (max_count - len(row)) // 2
    print(' ' * side_space, end='')
    print(row, end='')
    print(' ' * side_space)