from collections import deque

n=int(input())
card=deque(range(1,n+1))

while len(card)>1:
    card.popleft()
    tmp=card.popleft()
    card.append(tmp)

print(card[0])