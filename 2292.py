n=int(input())
bee=1
cnt=0
house=1

while True:
    house = house+cnt*6
    if n <= house:
        print(bee)
        break
    else:
        cnt+=1
        bee+=1