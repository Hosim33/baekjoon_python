n=int(input())
result=list(0 for j in range(n))
for i in range(n):
    name = []
    number = []
    yangjojang=int(input())
    school=[input() for _ in range(yangjojang)]
    for k in range(yangjojang):
        a,b=school[k].split()
        name.append(a)
        number.append(int(b))
        if max(number)==number[k]:
            answer=k
    print(name[answer])
