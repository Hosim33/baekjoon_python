n=int(input())
words= set(input() for _ in range(n))
words= list(words)
words.sort()
words.sort(key=len)
for i in words:
    print(i)