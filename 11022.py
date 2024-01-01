a=int(input())
num_list = []

for i in range(a):
    b, c=map(int,input().split())
    num_list.append("{0} + {1} = {2}".format(b,c,b+c))

for i in range(a):
    print("Case #{0}: {1}".format(i+1,num_list[i]))