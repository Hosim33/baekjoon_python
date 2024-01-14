star=int(input())
backup=star
for i in range(star):
    print(" "*(star-1),end="")
    print("*" *(i+1))
    star-=1
for j in range(backup-1):
    print(" " * (j+1), end="")
    print("*" * (backup-1))
    backup-=1

