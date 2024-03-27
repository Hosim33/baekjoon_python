import sys
input=sys.stdin.readline

n=int(input())
companylog={}

for _ in range(n):
    people,case=map(str, input().split())
    if case=="enter":
        companylog[people] = True
    else: del companylog[people]

person = sorted(companylog, reverse=True)

for j in person:
    print(j)