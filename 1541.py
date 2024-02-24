def f(x):
    return -x
math= input()
numbers= list()


if "-" not in math:
    tmp=map(int,math.split("+"))
    print(sum(tmp))
else:
    tmp = math.split("-")
    for i in tmp:
        numbers.append(sum(map(int, i.split(("+")))))
    numbers[0] *=-1
    print(sum(map(f,numbers)))