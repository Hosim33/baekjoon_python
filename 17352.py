import sys
input=sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    else: return x

N = int(input())
parent = [i for i in range(N+1)]

for _ in range(N-2):
    a, b = map(int, input().split())
    p1 = find(a)
    p2 = find(b)
    if p1 == p2:
        continue
    parent[p1] = p2

answer = []
for j in range(1, N+1):
    if j == parent[j]:
        answer.append(j)

print(*answer)