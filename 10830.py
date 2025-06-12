import math
from sys import stdin as s
s = open("input.txt", "r")
N, B = map(int, s.readline().split())

matrix = []
for _ in range(N):
    row = map(int, s.readline().split())
    matrix.append(list(row))

def multiplication(m1, m2):
    output = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                output[i][j] += m1[i][k] * m2[k][j]
    return output

def recursive(count):
    if count == 1: return matrix
    elif count == 2: return multiplication(matrix, matrix)

    unit = int(math.sqrt(count))
    output = multiplication(recursive(unit), recursive(unit))

    rest = count - unit - unit
    if rest > 0:
        output = multiplication(output, recursive(rest))
    
    return output

output = recursive(B)
for row in output:
    for num in row:
        print(num % 1000, end=' ')
    print()