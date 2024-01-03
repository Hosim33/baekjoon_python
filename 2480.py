dice=list(map(int, input().split()))
price=0
if(dice[0]==dice[1]):
    if(dice[1]==dice[2]):
        price=10000+1000*dice[0]
    elif(dice[1]!=dice[2]):
        price=1000+dice[1]*100
else:
    if(dice[0]==dice[2]):
        price=1000+dice[2]*100
    elif (dice[1] != dice[2]):
        price = max(dice) * 100
    else:
        price=1000+dice[1]*100

print(price)
