res = True
pre = 0
while(True):
    cur = int(input())
    if (cur == 0): break
    if (cur < pre):
        res = False
        break
    pre = cur
if (res):
    print("YES")
else:
    print("NO")