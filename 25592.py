n=int(input())
i=1
j=0

while(True):
    if n-i>=0:
        if n==0 and j%2==0:
            print(0)
            break
        elif n==0 and j%2!=0:
            print(i+1)
            break
        n-=i
        j+=1
        i+=1
    else:
        if j%2!=0:
            print(0)
            break
        else:
            print(i-n)
            break
