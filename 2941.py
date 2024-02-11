import sys
input=sys.stdin.readline

eng=input()
wl=["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in wl:
    if eng.count(i)!=0:
        eng=eng.replace(i,"*")

print(len(eng)-1)
