WU=[int(input()) for _ in range(10)]
KU=[int(input()) for _ in range(10)]
WU.sort(reverse=True)
KU.sort(reverse=True)
a, b=0,0
for i in range(3):
   a+=WU[i]
   b+=KU[i]
print(a,b)