numbers=[int(input()) for _ in range(7)]
answer=0
min=100
for i in numbers:
    if i%2>0:
        answer+=i
        if min>i: min=i
if answer!=0:
    print(answer)
    print(min)
else: print(-1)