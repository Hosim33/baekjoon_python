import math

fac=int(input())
result = math.factorial(fac)
result=str(result)
l=len(result)

if l==1: print(0)
for i in range(l-1,0,-1):
    if result[i]=='0':
        continue
    else:
        print(l-1-i)
        break