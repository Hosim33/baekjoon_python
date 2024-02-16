a, b = map(int, input().split())
c=list(map(int, input().split()))
c.sort(reverse=True)

answer=0
for i in range(len(c)):
    for j in range(i+1,len(c)):
        for k in range(j+1,len(c)):
            if c[i]+c[j]+c[k]<=b:
                answer=max(answer,c[i]+c[j]+c[k])

print(answer)
