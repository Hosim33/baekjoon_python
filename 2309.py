import sys
input = sys.stdin.readline
fake1=0
fake2=0

kid=[int(input()) for _ in range(9)]
sum=sum(kid)

for j in range(8):
  for k in range(j+1, 9):
    if sum - (kid[j] + kid[k]) == 100:
      fake1 = kid[j]
      fake2 = kid[k]
      break

kid.remove(fake1)
kid.remove(fake2)
kid.sort()
for j in kid:
    print(j)