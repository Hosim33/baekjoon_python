import sys
from heapq import heappush, heappop
input=sys.stdin.readline
n=int(input())
card=[]

for i in range(n):
    heappush(card, int(input()))

if n==1:
    print(0)
else:
    cnt=0
    while len(card) > 1:
        one = heappop(card)
        two = heappop(card)
        cnt += one+two
        heappush(card, one + two)
    print(cnt)