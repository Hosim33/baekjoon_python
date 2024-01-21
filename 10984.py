t=int(input())
for i in range(t):
    n=int(input())
    total = 0
    credit = 0
    for j in range(n):
        a,b=map(float, input().split())
        total += a
        credit += a*b
    print(int(total), round(credit/total,1))