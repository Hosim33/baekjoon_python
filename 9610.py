n=int(input())
point = [input() for _ in list(range(n))]
result=[0,0,0,0,0]
for i in range(len(point)):
    a, b = map(int, point[i].split())
    if a==0 or b==0: result[4]+=1
    elif 0<a and 0<b: result[0]+=1
    elif 0<a and 0>b: result[3]+=1
    elif 0<b and 0>a: result[1]+=1
    else: result[2]+=1

for j in range(0,4,1):
    print("Q"+str(j+1)+": " + str(result[j]))

print("AXIS: "+str(result[4]))