start=int(input())
fin=int(input())

numbers=list()
for i in range(start,fin+1):
    check=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                check +=1
                break
        if check==0: numbers.append(i)
if len(numbers)>0:
    print(sum(numbers))
    print(numbers[0])
else: print(-1)
