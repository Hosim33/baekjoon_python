result=1
for i in range(3):
    a=int(input())
    result*=a

result=str(result)
for j in range(10):
    count=0
    for k in range(len(str(result))):
        if str(j)==result[k]:
            count+=1
    print(count)
