import heapq, sys
input=sys.stdin.readline

N,H,T=map(int,input().split())
cnt=0
heap=[]

for _ in range(N):
    a=int(input())
    heapq.heappush(heap, -a)

for i in range(T):
    if heap[0]==-1 or -heap[0]<H:
        continue
    else:
        heapq.heapreplace(heap, -(-heap[0]//2))
        cnt+=1

if H>-heap[0]:
    print("YES")
    print(cnt)
else:
    print("NO")
    print(int(-heap[0]))