#회의 개수
N=int(input())
info=[list(map(int,input().split())) for _ in range(N)]

info.sort(key = lambda x: (x[1], x[0]))
choice=[0, 0]

cnt=1
choice[1]=info[0][1]

for i in range(1, N):
    if info[i][0] >= choice[1]:
        cnt+=1
        choice[1]=info[i][1]

print(cnt)