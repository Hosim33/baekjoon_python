price=int(input())
books=[int(input()) for _ in range(9)]

for i in range(len(books)):
    price-=books[i]
print(price)