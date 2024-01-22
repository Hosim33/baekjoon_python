max=0
check=0
for i in range(5):
    a,b,c,d=map(int,input().split())
    if a+b+c+d >= max:
        max=a+b+c+d
        check=i+1
print(check, max)