answer=[1,1,2,2,2,8]
chess=list(map(int, input().split()))

result=[]
for i in range(6):
    result.append(answer[i]-chess[i])
    print(result[i],end=" ")