import math

a=int(input())
b=int(input())
sum=[0,0]

c=math.ceil(math.sqrt(a))
sum[1]=c*c
while c<=math.sqrt(b):
    sum[0]+=c*c
    c = c + 1
if int(math.sqrt(a))==int(math.sqrt(b)):
    print(-1)
else:
    print(sum[0])
    print(sum[1])