big=[]

while(1):
    a, b = map(int, input().split())
    if a==0 and b==0: break
    elif a>b: big.append("Yes")
    else: big.append("No")

for i in big:
    print(i)