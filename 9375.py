import sys
input=sys.stdin.readline
T = int(input())

for _ in range(T):
    cloth = {}
    result = 1
    n = int(input())
    for _ in range(n):
        name, type = map(str,(input().split()))

        if not type in cloth:
            cloth[type] = 1
        else:
            cloth[type] += 1

    for i in cloth:
        result *= (cloth[i] + 1) #옷 종류별 수에서 그 옷 안 입은 경우 1 더하고 종류만큼 곱하기

    print(result - 1) # 0개 입은 거 제외