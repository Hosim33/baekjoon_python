n=int(input())
dice=[(input()) for _ in range(n)]
tmp=list()
price=list(range(n))
for i in range(n):
    tmp=dice[i].split()
    for j in range(len(tmp)):
        tmp[j] = int(tmp[j])
    if tmp[0]==tmp[1]==tmp[2]:
        price[i] = 10000 + 1000 * tmp[0]
    elif tmp[0]==tmp[1] or tmp[0]==tmp[2]:
        price[i] = 1000 + tmp[0] * 100
    elif(tmp[1]==tmp[2]):
        price[i] = 1000 + tmp[1] * 100
    else: price[i]=max(tmp)*100
print(max(price))
