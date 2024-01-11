n=int(input())
check=0
result=0
for i in range(1,n+1):
    check+=i
    result+=1
    if check>n:
        result-=1
        break
print(result)