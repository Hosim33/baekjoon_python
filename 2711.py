t=int(input())
for i in range(t):
    a,b=map(str,input().split(" "))
    print(b[:int(a)-1],end="")
    print(b[int(a)::])