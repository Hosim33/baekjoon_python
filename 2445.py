star=int(input())
for j in range(1,star+1):
    print("*"*j+" "*(star-j)+" " * (star - j)+"*" * j)
for k in range(star-1,0,-1):
    print("*"*k+" "*(star-k)+" " * (star - k)+"*" * k)