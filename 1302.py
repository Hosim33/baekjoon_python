N=int(input())
book={}
keyword=[]

for i in range(N):
    a=input()
    if a in book:
        book[a]+=1
    else: book[a]=1

bs=max(book.values())

for key,value in book.items():
    if value==bs:
        keyword.append(key)

keyword.sort()
print(keyword[0])