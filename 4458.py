n=int(input())
for i in range(n):
    line=input()
    print(line[0].upper(),end="")
    print(line[1::])