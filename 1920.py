import sys
input=sys.stdin.readline

n=int(input())
one=list(map(int, input().split()))
m=int(input())
two=list(map(int, input().split()))

sone=set(one)

for i in two:
    if i in sone: print(1)
    else: print(0)