problem=int(input())
score=list(map(int,input().split()))
answer, tmp=0,1
for i in range(problem):
    if score[i]==1:
        answer+=tmp
        tmp+=1
    else: tmp=1
print(answer)