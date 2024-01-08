n=int(input())
y,k = 0,0
baseball=[input() for _ in range(n*9)]

for i in range(n):
    y, k = 0, 0
    for j in range(9):
        a,b=map(int, baseball[i*9+j].split())
        y+=a
        k+=b
    if y>k: print("Yonsei")
    elif y<k: print("Korea")
    else: print("Draw")
