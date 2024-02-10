a,b=map(int,input().split())
words=[input() for _ in range(a)]
check=[input() for _ in range(b)]
result=0
for i in words:
    result+=check.count(i)
print(result)