import sys
input = sys.stdin.readline

N=int(input()) #재료 개수
M=int(input()) #갑옷을 만드는데 필요한 수
num=list(map(int,(input().split()))) #재료 고유 번호

num.sort()
left= 0
right = N-1
answer=0

while left < right:
    sum_num = num[left] + num[right]
    if sum_num < M:
        left += 1
    elif sum_num > M:
        right -= 1
    else:
        answer += 1
        left += 1
        right -= 1

print(answer)