n=int(input())
for i in range(n):
    v,e=map(int,input().split())
    answer=(v-e-2)*-1
    print(answer)