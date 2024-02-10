import sys
input = sys.stdin.readline

n,m=map(int, input().split())
dic={}

for _ in range(n):
    site, ps = input().split()
    dic[site]=ps

for _ in range(m):
    search = input().rstrip()
    print(dic[search])