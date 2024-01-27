numbers=[input() for _ in range(10)]
train=[0] * 10
for i in range(10):
    a,b=map(int, numbers[i].split())
    if i == 0:
        train[i]+=b
        train[i]-=a
    else:
        train[i]=train[i-1]+b-a
print(max(train))