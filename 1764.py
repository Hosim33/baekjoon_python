n,m=map(int, input().split())
np=[input() for _ in range(n)]
mp=[input() for _ in range(m)]

intersection = set(np) & set(mp)
answer = sorted(list(intersection))
print(len(answer))
for i in answer:
    print(i)