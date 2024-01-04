n=int(input())
mars_math=[(input()) for _ in range(n)]
tmp=list()
result=list(range(n))

for i in range(len(mars_math)):
    tmp=mars_math[i].split()
    result[i] = tmp[0]
    for j in range(len(tmp)-1):
        if bool(tmp[j+1])!=0:
            if(tmp[j+1]=="@"):
                result[i]=float(result[i])*3
            elif(tmp[j+1]=="#"):
                result[i]=float(result[i])-7
            else:result[i]=float(result[i])+5
    tmp=list()
for k in range(n):
    print('%.2f'%result[k])