import sys
input=sys.stdin.readline

sys.setrecursionlimit(10 ** 5)

N, M = map(int,input().split())
s, e = map(int,input().split())
bridge = [ list(map(int,input().split())) for _ in range(M)]

bridge = sorted(bridge, key=lambda x: x[2])

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return
    parent[root_x] = root_y

parent = list(range(N + 1))
last = 0

while find(s) != find(e) and bridge:
    x, y, d = bridge.pop()
    last = d
    union(x, y)

result = last if find(s) == find(e) else 0
print(result)