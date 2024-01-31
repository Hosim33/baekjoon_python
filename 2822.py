score=[int(input()) for _ in range(8)]
answer=sorted(score, reverse=True)
result=0
check=[0,0,0,0,0]
for i in range(5):
    check[i] = score.index(answer[i])
    result+=answer[i]
print(result)
check.sort()
for j in range(5):
    print(check[j]+1,end=" ")