word=input()
target=['a','e','i','o','u']
answer=0
for i in range(len(word)):
    if word[i] in target:
        answer+=1
print(answer)
