import sys
from collections import deque

def Solution():
    dy = (-1, 0, 1, 0)
    dx = (0, 1, 0, -1)
    res = 0
    input = sys.stdin.readline
    n, m = map(int, input().split())
    land = [list(map(str, input())) for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if land[y][x] == "L":
                if 0 <= y - 1 < n and 0 <= y + 1 < n and \
                        land[y - 1][x] == "L" and land[y + 1][x] == "L":
                    continue
                if 0 <= x - 1 < m and 0 <= x + 1 < m and \
                        land[y][x - 1] == "L" and land[y][x + 1] == "L":
                    continue
                q = deque()
                q.append((y, x, 0))
                toVisit = [[True for _ in range(m)] for _ in range(n)]
                toVisit[y][x] = False
                while q:
                    ty, tx, cnt = q.popleft()
                    for d in range(4):
                        tmpY = ty + dy[d]
                        tmpX = tx + dx[d]
                        if n > tmpY >= 0 and m > tmpX >= 0 and \
                                toVisit[tmpY][tmpX] and land[tmpY][tmpX] == "L":
                            toVisit[tmpY][tmpX] = False
                            q.append((tmpY, tmpX, cnt + 1))
                res = max(res, cnt)
    return res

if __name__ == "__main__":
    print(Solution())