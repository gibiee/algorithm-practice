from sys import stdin as s
s = open("input.txt", "rt")

n, m = map(int, s.readline().split())
parents = list(range(n))
def find_parent(x):
    global parents
    parent = parents[x]
    if parent == x:
        return x
    else:
        parents[x] = find_parent(parent)
        return parents[x]

for i in range(m):
    a, b = map(int, s.readline().split())
    parent_a = find_parent(a)
    parent_b = find_parent(b)
    if parent_a == parent_b:
        print(i+1)
        break

    parent_ab = min(parent_a, parent_b)
    parents[parent_a], parents[parent_b] = parent_ab, parent_ab
else:
    print(0)