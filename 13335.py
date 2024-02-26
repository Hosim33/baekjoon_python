from collections import deque
import sys
input=sys.stdin.readline

#n=트럭개수,w=다리길이,L=버틸 수 있는 하중

n,w,L=map(int,input().split())
weight=list(map(int,input().split()))
time=0
bridge = [0] * w

while bridge:
    time += 1
    bridge.pop(0)
    if weight:
        if sum(bridge) + weight[0] <= L:
            bridge.append(weight.pop(0))
        else:
            bridge.append(0)
print(time)
