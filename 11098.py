n=int(input())
people=""
for i in range(n):
    max=0
    m=int(input())
    for j in range(m):
        a,b=input().split()
        if int(a)>int(max):
            max=a
            people=b
    print(people)