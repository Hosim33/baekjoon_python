answer=[0,0,0,0]
for i in range(4):
    a, b = map(int, input().split())
    if i==0:answer[i]=b
    else:
        answer[i]=answer[i-1]+b-a
print(max(answer))
