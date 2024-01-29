import statistics

numlist=[int(input()) for _ in range(10)]
print(sum(numlist)//10)
print(statistics.mode(numlist))