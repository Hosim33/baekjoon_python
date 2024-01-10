import math

n=int(input())
numbers=[input() for _ in range(n)]
for i in range(len(numbers)):
    a,b=map(int, numbers[i].split())
    c=a*b
    d=math.gcd(a,b)
    if a==1: print(b)
    elif a==b: print(b)
    else: print(c//d)