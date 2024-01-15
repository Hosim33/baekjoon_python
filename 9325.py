n=int(input())
for i in range(n):
    price=int(input())
    option=int(input())
    if option>0:
        a=[input() for _ in range(option)]
        for j in range(option):
            b,c=a[j].split()
            price+=int(b)*int(c)
        print(price)
    else: print(price)