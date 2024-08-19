from itertools import *

N,K=map(int,input().split())
A=list(map(int,input().split()))
cnt=0

answer = list(permutations(A, N))

for i in range(len(answer)):
    health=500
    for j in range(N):
        health += answer[i][j] - K
        if health < 500:
            break
        if j == N-1 and health >= 500:
            cnt += 1

print(cnt)