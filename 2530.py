a, b, c=map(int,input().split())
d=int(input())
e=d//60
f=d%60

b=b+e
c=c+f
b=b+c//60
c=c%60
a=a+b//60
b=b%60
a=a%24

print(a, b, c)