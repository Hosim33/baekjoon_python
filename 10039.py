n=int(input())
num_list=[int(input()) for _ in range(n)]
result=0
for i in num_list:
    if(i<40):
        i=40
    result+=i
print(result//5)
