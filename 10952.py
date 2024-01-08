plus=[]

while(1):
    a, b = map(int, input().split())
    if a==0 and b==0: break
    else: plus.append(a+b)

for i in plus:
    print(i)