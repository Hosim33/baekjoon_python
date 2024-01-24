memo=input()
answer=list(map(str, memo.split("-")))
for i in range(len(answer)):
    print(answer[i][0],end="")