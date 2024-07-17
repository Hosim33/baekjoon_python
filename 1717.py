import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n,m=map(int, input().split())
parent=[i for i in range(n+1)]

def union(b,c):
    b = find(b)
    c = find(c)
    if b < c:
        parent[c] = b
    else: parent[b] = c

def find(b):
    if parent[b] != b:
        parent[b] = find(parent[b])
    return parent[b]

for i in range(m):
    a,b,c=map(int,input().split())
    if a==0:
        union(b,c)
    else:
        if find(b) == find(c):
            print("YES")
        else: print("NO")

