n=int(input())
tree={}

for i in range(n):
    a,b,c = map(str,input().split()) #root, left, right
    tree[a]= b,c

def pre(stnd): #stnd => start node
    if stnd !=".":
        print(stnd, end="")
        pre(tree[stnd][0])
        pre(tree[stnd][1])

def ino(stnd):
    if stnd !=".":
        ino(tree[stnd][0])
        print(stnd, end="")
        ino(tree[stnd][1])

def post(stnd):
    if stnd !=".":
        post(tree[stnd][0])
        post(tree[stnd][1])
        print(stnd, end="")

pre('A')
print("")
ino('A')
print("")
post('A')
