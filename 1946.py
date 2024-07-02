import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    N=int(input())
    emp=[list(map(int, input().split())) for _ in range(N)]

    emp.sort()
    top = emp[0][1] # 서류 1등 면접 등수
    cnt = 1 # 서류 1등은 무조건 합격이기 때문에 1

    for i in range(1,N):
        if top > emp[i][1]:
            cnt+=1
            top = emp[i][1]
    print(cnt)