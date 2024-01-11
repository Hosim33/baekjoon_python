while(True):
    numbers = []
    a=int(input())
    if a==-1: break
    for i in range(1,a):
        if a%i==0:
            numbers.append(i)
    if sum(numbers) == a:
        for j in numbers:
            if j==numbers[0]:
                print(a,"=",j, end=" ")
            else: print("+",j, end=" ")
    else: print(a,"is NOT perfect.")