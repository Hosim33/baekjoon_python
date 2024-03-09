n=int(input())
point=[list(map(int,input().split())) for _ in range(n)]
point.sort()
for a,b in point:
    print(a,b)