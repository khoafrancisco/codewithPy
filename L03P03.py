hightest = -1
lowest = 11
while (True):
    p = int(input())
    if (p == -1): break
    if p > hightest: hightest = p;
    if p < lowest: lowest = p;
print(hightest, lowest)