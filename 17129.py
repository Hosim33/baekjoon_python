from collections import deque
n,m=map(int,input().split())
food = [list(map(int, input().strip())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
q = deque()
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y):
    global ans
    q.append([x,y])
    visited[x][y]+=1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and food[nx][ny] != 1 and not visited[nx][ny]:
                    q.append([nx,ny])
                    visited[nx][ny]= visited[x][y] +1
                    if food[nx][ny] in (3,4,5):
                        print('TAK')
                        print(visited[x][y])
                        exit()
    print('NIE')

for i in range(n):
    for j in range(m):
        if food[i][j]==2:
            bfs(i,j)

#pypy3