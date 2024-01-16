numbers=[int(input()) for _ in range(10)]
for i in range(10): numbers[i]=numbers[i]%42
a=set(numbers)
print(len(a))