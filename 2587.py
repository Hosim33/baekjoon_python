numbers=[int(input()) for _ in range(5)]
average=0
for i in numbers:
    average+=i
average=average//5
numbers.sort()
print(average)
print(numbers[2])