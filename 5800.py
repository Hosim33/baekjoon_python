K=int(input())
for i in range(K):
    N = list(map(int, input().split()))
    gap=[0]*(N[0])
    N.pop(0)
    N.sort(reverse=True)
    for j in range(len(N)-1):
        gap[j]=N[j]-N[j+1]
    print("Class",i+1)
    print("Max", str(max(N))+",", "Min", str(min(N))+",","Largest gap",max(gap))