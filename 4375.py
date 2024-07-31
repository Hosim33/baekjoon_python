a = '1'
b = ''

while True:
    try:
        n = int(input())
        while True:
            b += a
            c = int(b)
            if c%n==0:
                print(len(str(c)))
                b = ''
                break
    except EOFError:
        break