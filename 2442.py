star=int(input())
for i in range(star):
    print(" "*(star-1),end="")
    print("*"*(2*i+1))
    star-=1