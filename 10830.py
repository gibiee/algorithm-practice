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
            output[i][j] %= 1000
    return output

def recursive(count):
    if count == 1: return matrix
    elif count == 2: return multiplication(matrix, matrix)

    half = recursive(count//2)
    output = multiplication(half, half)
    if count % 2 == 1:
        output = multiplication(output, matrix)
    
    return output

output = recursive(B)
for row in output:
    for num in row:
        print(num % 1000, end=' ')
    print()