import sys
input = sys.stdin.readline

N=int(input())
card=list(map(int,input().split()))

dp = [1] * N

for i in range(1, N):
    tmp=0
    for j in range(i):
        if card[j] < card[i]:
            tmp = max(tmp, dp[j])
        dp[i] = tmp + 1

print(max(dp))