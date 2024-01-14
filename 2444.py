star=int(input())
backup=star
for i in range(star):
    print(" "*(star-1),end="")
    print("*"*(2*i+1))
    star-=1
for j in range(1,backup):
    backup -= 1
    print(" " *j,end="")
    print("*"*(2*backup-1))