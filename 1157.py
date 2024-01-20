word=input().upper()
unique=list(set(word))
check=[]
for i in unique:
  count = word.count(i)
  check.append(count)

if check.count(max(check)) >= 2:
  print("?")
else:
  print(unique[check.index(max(check))])