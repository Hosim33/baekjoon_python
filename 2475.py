nums=list(map(int, input().split()))
answer=[]
for i in nums:
    answer.append(i*i)
print(sum(answer)%10)