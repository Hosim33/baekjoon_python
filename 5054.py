t = int(input())
for i in range(t):
    n=int(input())
    store=list(map(int, input().split()))
    print((max(store)-min(store))*2)