a,b=map(int, input().split())
array=list()

for i in range(b+1):
    for j in range(i):
        array.append(i)

if a!=0: a=a-1
print(sum(array[a:b]))