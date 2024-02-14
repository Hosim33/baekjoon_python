check=[int(input()) for _ in range(3)]
a=check[0]
b=check[1]
c=check[2]
if a+b+c!=180:
    print("Error")
elif a==b & b==c & a==c:
    print("Equilateral")
elif a==b or b==c or a==c:
    print("Isosceles")
else: print("Scalene")