n,m=map(int, input().split())
#n은 바구니 개수고 m은 공을 넣는 횟수
basket=[0]*n

for o in range(m):
    i,j,k=map(int, input().split())
    for p in range(i-1,j):
        basket[p]=k

for q in basket:
    print(q, end=" ")


