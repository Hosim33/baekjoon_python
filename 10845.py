import sys
input = sys.stdin.readline

N=int(input())
Queue=[]
for i in range(N):
    a=list(map(str,input().split()))
    if a[0]=="push":
        Queue.append(a[1])
    elif a[0]=="front":
        if len(Queue)==0: print(-1)
        else: print(Queue[0])
    elif a[0] == "back":
        if len(Queue) == 0: print(-1)
        else: print(Queue[-1])
    elif a[0]=="size": print(len(Queue))
    elif a[0]=="pop":
        if len(Queue) == 0: print(-1)
        else:
            print(Queue[0])
            del Queue[0]
    else:
        if len(Queue)==0: print(1)
        else: print(0)

