from sys import stdin as s
s = open("input.txt", "rt")

T = int(s.readline().strip())

def find_parent(f):
    global info
    if info[f]['parent'] != f:
        info[f]['parent'] = find_parent(info[f]['parent'])
    return info[f]['parent']

def union(f1, f2):
    f1_parent = find_parent(f1)
    f2_parent = find_parent(f2)
    if f1_parent != f2_parent:
        union_parent = f1_parent
        union_friends = info[f1_parent]['friends'] + info[f2_parent]['friends']
        info[f1_parent]['parent'], info[f2_parent]['parent'] = union_parent, union_parent
        info[f1_parent]['friends'], info[f2_parent]['friends'] = union_friends, union_friends
    return info[f1_parent]['friends']

for _ in range(T):
    F = int(s.readline().strip())
    info = {}
    for __ in range(F):
        f1, f2 = s.readline().split()
        info.setdefault(f1, {'parent': f1, 'friends': 1})
        info.setdefault(f2, {'parent': f2, 'friends': 1})
        print(union(f1, f2))