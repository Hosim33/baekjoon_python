word=input()
eng='abcdefghijklmnopqrstuvwxyz'
for i in range(26):
    print(word.count(eng[i]),end=" ")