a=int(input())
cow=[]
for j in range(a):
    cow.append(list(map(int,input().split())))
cow.sort()
time=0
for i in range(a):
    b,c=cow[i][0],cow[i][1]
    if time<=int(b):
        time=int(b)+int(c)
    else: time+=int(c)
print(time)