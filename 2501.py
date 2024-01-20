a,b=map(int, input().split())
numbers=[]

for i in range(1,a+1):
    if a%i==0:
        numbers.append(i)
    if len(numbers) > b:
        break

if len(numbers)<b:
    print(0)
else: print(numbers[b-1])