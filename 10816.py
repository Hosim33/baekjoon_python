import sys
input=sys.stdin.readline

a=int(input())
origin=list(map(int,input().split()))
b=int(input())
after=list(map(int,input().split()))

cards=dict()

for i in origin:
    if i in cards:
        cards[i] +=1
    else:
        cards[i] =1

for j in after:
    result = cards.get(j)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")