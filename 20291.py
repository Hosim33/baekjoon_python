num=int(input())
filelist=[input() for _ in range(num)]
fd=dict()

for i in filelist:
    check=i.split('.')
    if fd.get(check[-1]):
        fd[check[-1]]+=1
    else: fd[check[-1]]=1
fd=sorted(fd.items())

for j in fd:
    print(j[0], j[1])