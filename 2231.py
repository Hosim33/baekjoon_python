n=int(input())
check=0
for i in range(n):
    for j in range(len(str(i))):
        i=str(i)
        check+=int(i[j])
    check+=int(i)
    if check==n:
        print(i)
        break
    else:
        if i==str(n-1):
            print(0)
        check=0