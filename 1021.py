from collections import deque
import sys
input = sys.stdin.readline

n,m=map(int, input().split())
number=list(map(int,input().split()))
dq = deque([i for i in range(1, n+1)])

count=0
for i in number:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2:  # 뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈것보다 작을때는 왼쪽으로 움직여야 최소
                while dq[0] != i:
                    dq.append(dq.popleft())
                    count += 1
            else:   # 뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈것보다 클때는 오른쪽으로 움직여야 최소
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    count += 1
print(count)