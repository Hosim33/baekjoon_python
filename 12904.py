S = input()
T = input()

cnt=len(T) - len(S)

for i in range(cnt):
    if T[-1] == 'A':
        T=T[0:-1]
    elif T[-1] == 'B':
        T = T[0:-1]
        T = T[::-1]

if S==T:
    print(1)
else: print(0)