import sys
a, b = map(int, sys.stdin.readline().split())

Aset= set(map(int, sys.stdin.readline().split()))
Bset = set(map(int, sys.stdin.readline().split()))


print(len(Aset - Bset))
print(*(sorted(Aset - Bset)))