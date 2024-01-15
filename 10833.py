apple=int(input())
answer=0
for i in range(apple):
    a,b=map(int,input().split())
    if b/a>=1:
        answer+=b%a
    else: answer+=b
print(answer)