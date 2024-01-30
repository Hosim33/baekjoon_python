N, K=map(int,input().split())
coin=[int(input()) for _ in range(N)]
coin.reverse()
answer=0
for i in coin:
    if K>=i:
        answer+=K//i
        K-=i*(K//i)
    else: continue
print(answer)