n,d=input().split()
count=0
for i in range(int(n),0,-1):
    count+=str(i).count(d)
print(count)