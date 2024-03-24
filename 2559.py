import sys
input=sys.stdin.readline

n,k=map(int,input().split())
temp=list(map(int,input().split()))

sum = sum(temp[:k])
answers = [sum]

for i in range(n-k):
    sum = sum-temp[i]+temp[i+k]
    answers.append(sum)

print(max(answers))