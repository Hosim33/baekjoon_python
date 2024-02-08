n,m=map(int, input().split())
price=list()
result=[0]*m
for i in range(m):
    egg=int(input())
    price.append(egg)
price.sort()
if n<m:
    for j in range(m):
        if n>m-j:
            result[j] = price[j] *(m-j)
        else: result[j] = price[j]*n
else:
    for j in range(m):
        result[j] = price[j] * (m-j)
answer=max(result)
check=result.index(answer)
print(price[check],answer)