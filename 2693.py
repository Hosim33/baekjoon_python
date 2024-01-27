t=int(input())
for i in range(t):
    numbers=list(map(int, input().split()))
    numbers.sort()
    print(numbers[7])