import sys
input=sys.stdin.readline

n=int(input())
bar=[int(input()) for _ in range(n)]
answer=1
bar.reverse()
last=bar[0]

for i in range(n):
    if bar[i]>last:
        last=bar[i]
        answer+=1

print(answer)