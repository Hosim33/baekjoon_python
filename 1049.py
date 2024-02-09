import math

n,m=map(int,input().split())
price=list()
six=list()
one=list()
for i in range(m):
    a, b = map(int, input().split())
    price.append(b * n)
    six.append(a)
    one.append(b)
one.sort()
six.sort()
c=math.floor(n/6)
d=n-c*6
price.append(six[0] * c +one[0]*d)
price.append(six[0]*(c+1))
print(min(price))