while(True):
    n=input()
    if n == "0": break
    m=n[::-1]
    if m==n: print("yes")
    else: print("no")
