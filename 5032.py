e,f,c=map(int,input().split())
i=0
e+=f
while e>=c:
 p=e//c
 q=e%c
 e=p+q
 i+=p
print(i)