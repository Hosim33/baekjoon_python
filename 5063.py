n=int(input())
advertise=[(input()) for _ in range(n)]
tmp=list()

for i in range(n):
    tmp=advertise[i].split()
    if int(tmp[1])-int(tmp[2])>int(tmp[0]):
        print("advertise")
    elif int(tmp[1])-int(tmp[2])==int(tmp[0]):
        print("does not matter")
    else: print("do not advertise")