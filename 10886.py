n=int(input())
cute=[(input()) for _ in range(n)]

one = cute.count('1')
zero = cute.count('0')

if one>zero: print("Junhee is cute!")
else: print("Junhee is not cute!")