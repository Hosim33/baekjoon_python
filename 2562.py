numbers=[int(input()) for _ in range(9)]
print(max(numbers))
for i in range(9):
    if(max(numbers)==numbers[i]): print(i+1)