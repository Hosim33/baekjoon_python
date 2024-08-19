import sys
input=sys.stdin.readline

p,m = map(int,input().split())
user = [ list(map(str,input().split())) for _ in range(p)]

rooms=[]

for i in range(p):
    if not rooms:
        rooms.append([[int(user[i][0]),user[i][1]]])
        continue

    enter = False

    for room in rooms:
        # 조건에 합당하면 넣어주기
        if len(room) < m and room[0][0] - 10 <= int(user[i][0]) <= room[0][0] + 10:
            room.append([int(user[i][0]),user[i][1]])
            enter = True
            break

    if not enter:
        rooms.append([[int(user[i][0]),user[i][1]]])

for room in rooms:
    room.sort(key=lambda x: x[1])

for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    for lv, name in room:
        print(lv, name)