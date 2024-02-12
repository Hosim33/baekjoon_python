t=int(input())
test=[input() for _ in range(t)]
check=0
for i in range(t):
    while(check==0):
        test[i] = test[i].replace("()", "")
        if test[i].count("()") == 0:
            check = 1
            if len(test[i])!=0:
                print("NO")
            else: print("YES")
    check=0