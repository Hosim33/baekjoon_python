t=int(input())
for j in range(t):
    numbers = list(map(int, input().split()))
    total = 0
    min = 100
    for i in range(7):
        if numbers[i]%2==0:
            total+=numbers[i]
            if min>numbers[i]:
                min=numbers[i]
    print(total, min)