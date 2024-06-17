import sys
import heapq
input=sys.stdin.readline

num=int(input())
heap=[]
for i in range(num):
    a=int(input())

    if a!=0:
        heapq.heappush(heap, -a)
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)