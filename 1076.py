color={'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'grey':8,'white':9}

answer=''
for j in range(3):
    a=input()
    if j==2: print(int(answer)*10**color[a])
    result = color[a]
    answer += str(result)