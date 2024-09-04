H, W, X, Y=map(int,input().split())
B_arr=[list(map(int,input().split())) for _ in range(H+X)]
A_arr=[[0]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        A_arr[i][j]=B_arr[i][j]

for k in range(X,H):
  for l in range(Y,W):
    A_arr[k][l] = B_arr[k][l] - A_arr[k-X][l-Y]

for m in range(H):
  for n in range(W):
    print(A_arr[m][n],end=" ")
  print("")