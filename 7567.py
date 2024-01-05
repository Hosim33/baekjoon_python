dish=input()
height=10
for i in range(len(dish)-1):
    if dish[i] == dish[i+1]:
        height+=5
    else: height+=10
print(height)