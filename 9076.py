t=int(input())
for i in range(t):
    numbers=list(map(int,input().split()))
    numbers.sort()
    numbers.pop(0)
    numbers.pop(3)
    if numbers[2]-numbers[0]>=4:
        print("KIN")
    else: print(sum(numbers))
