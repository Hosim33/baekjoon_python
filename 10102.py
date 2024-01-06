num=int(input())
result=input()
anum, bnum=0, 0

for i in range(len(result)):
    if result[i]=="B": bnum+=1
    else: anum+=1

if anum>bnum: print("A")
elif bnum>anum: print("B")
else: print("Tie")