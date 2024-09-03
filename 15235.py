N = int(input())
pizza = list(map(int, input().split()))

time = [0] * N

count = 0
index = 0

while 0 < sum(pizza):
    if pizza[index] != 0:
        pizza[index] -= 1
        count += 1

    if pizza[index] == 0 and time[index] == 0:
        time[index] = count

    index += 1

    if index == len(pizza):
        index = 0

print(*time)