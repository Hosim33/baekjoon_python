n=int(input())
score=list(map(int,input().split()))
answer=0
max=max(score)
for i in range(n):
    answer+=score[i]/max*100

print(answer/n)