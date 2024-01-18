numbers=[0,1]
n=int(input())
if n>=2:
    for i in range(2,n+1):
        a=numbers[i-2]+numbers[i-1]
        numbers.append(a)
print(numbers[n])
