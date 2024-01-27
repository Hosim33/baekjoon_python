count=int(input())
numbers=list(map(int, input().split()))
if count>1:
    print((min(numbers)*max(numbers)))
else:
    print(numbers[0]*numbers[0])