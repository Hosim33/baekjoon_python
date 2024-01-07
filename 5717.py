friend=[]

while(1):
    a, b = map(int, input().split())
    if a==0 and b==0: break
    else: friend.append(a+b)

for i in friend:
    print(i)