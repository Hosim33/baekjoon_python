t=int(input())
alpha=[input() for _ in range(t)]
for i in range(t):
    a,b=map(str, alpha[i].split())
    print("Distances: ",end="")
    for j in range(len(a)):
        if (ord(b[j])-ord(a[j]))>=0:
            print(ord(b[j]) - ord(a[j]), end=" ")
        else: print(26+ord(b[j]) - ord(a[j]), end=" ")
    print()