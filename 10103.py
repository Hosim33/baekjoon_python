n=int(input())
dice=[input() for _ in range(n)]
score=[100,100]
for i in range(len(dice)):
    a,b=map(int, dice[i].split())
    if a>b: score[1]=score[1]-a
    elif a<b: score[0]=score[0]-b
print(score[0])
print(score[1])