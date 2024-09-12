#부분합 1806
import sys
input=sys.stdin.readline

N,S = map(int,input().split())
arr = list(map(int,input().split()))

start,end = 0,1
sum=0
answer=100000

prefix_sum = [0]
for i in range(len(arr)): # O(N)
    prefix_sum.append(prefix_sum[i]+arr[i])

while start < N:
    if prefix_sum[end] - prefix_sum[start] < S:
        if end < N:
            end += 1
        else:
            start += 1
    else:
        answer = min(end-start, answer)
        start += 1

if answer == 100000:
    print(0)
else:
    print(answer)