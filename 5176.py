t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    s=[int(input()) for _ in range(a)]
    s=list(set(s))
    print(a-len(s))