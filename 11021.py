a=int(input())
num_list = []

for i in range(a):
    b, c=map(int,input().split())
    num_list.append(b+c)

for i in range(a):
    print("Case #{0}: {1}".format(i+1,num_list[i]))