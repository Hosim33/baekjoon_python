import sys
input=sys.stdin.readline

n,m=map(int,input().split())
p=[i for i in range(n)]
def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else: p[a] = b

def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]
answer = 0

for i in range(1,m+1):
    a,b=map(int, input().split())
    if find(a) == find(b):
        answer = i
        break
    union(a,b)

print(answer)
