t=int(input())
for i in range(t):
    n=int(input())
    answer=str(format(n, 'b'))
    answer=answer[::-1]
    for j in range(len(answer)):
        if answer[j]=='1':
            print(j)