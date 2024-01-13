star=int(input())
for i in range(star):
    star -= 1
    print(" " *i,end="")
    print("*"*(2*star+1))