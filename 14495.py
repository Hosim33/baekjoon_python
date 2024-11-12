num = int(input())
pib=[1,1,1]
ans = 0
for i in range(num):
    if i<3:
        continue
    m=pib[i-1] + pib[i-3]
    pib.append(m)

print(pib[num-1])