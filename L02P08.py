candy1, candy2, candy3, candy4 = map(int, input().split())

maxCandy = candy1
if (maxCandy < candy2):
    maxCandy = candy2
if (maxCandy < candy3):
    maxCandy = candy3
if (maxCandy < candy4):
    maxCandy = candy4

print(maxCandy)
