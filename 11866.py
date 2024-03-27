N,K=map(int,input().split())
num=list(range(1,N+1))
answer=[]
index=0

while len(num) != 0:
    index+=(K-1)
    index = index % len(num)
    answer.append(num.pop(index))

ans_str = str(answer)[1:-1]

print("<",end="")
print(ans_str,end="")
print(">",end="")
