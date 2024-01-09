n=int(input())
oxquiz=[input() for _ in range(n)]
score=list(0 for k in range(n))
for i in range(n):
    tmp=1
    for j in range(len(oxquiz[i])):
        if oxquiz[i][j]=="O":
            score[i] += tmp
            if j == (len(oxquiz[i]) - 1):
                break
            if oxquiz[i][j+1]=="O":
                tmp+=1
            else: tmp=1
    print(score[i])