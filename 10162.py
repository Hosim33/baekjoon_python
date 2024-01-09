time=int(input())
micro=[0,0,0]
while time!=0:
    if time<10: break
    micro[0]=time//300
    time = time % 300
    micro[1]=time//60
    time = time % 60
    micro[2]=time//10
    time = time % 10

if time==0: print(micro[0], micro[1], micro[2])
else: print("-1")