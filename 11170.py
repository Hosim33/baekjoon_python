t=int(input())
for i in range(t):
    n,m=map(int, input().split())
    count=0
    for j in range(n,m+1):
        a = str(j)
        count += a.count('0')
    print(count)