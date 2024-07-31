import sys
input = sys.stdin.readline

H, W = map(int,input().split())
sky = [ list(map(str,input())) for _ in range(H) ]
cloud = [[-1]*W for _ in range(H)]

for a in range(H):
    check=-1
    for b in range(W):
        if sky[a][b] == 'c':
            check = b
            cloud[a][b] = 0
        elif sky[a][b] == '.' and check >= 0:
            cloud[a][b] = b-check

for i in range(H):
    for j in range(W):
        print(cloud[i][j],end=" ")
    print()