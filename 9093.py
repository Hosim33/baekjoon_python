n=int(input())
eng=[input() for _ in range(n)]
for i in range(n):
    a=list()
    a=eng[i].split()
    for j in a:
        print(j[::-1],end=" ")
    print("")