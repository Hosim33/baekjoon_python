n=int(input())
birthday=[input() for _ in range(n)]
for i in range(n):
    a,b,c,d=birthday[i].split()
    if int(c)<10: c="0"+c
    if int(b) < 10: b = "0" + b
    birthday[i]=d+" "+c+" "+b+" "+a
birthday.sort()
e,f,g,h=birthday[n-1].split()
print(h)
e,f,g,h=birthday[0].split()
print(h)
    
