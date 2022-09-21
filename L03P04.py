import imp


import math

n = int(input())
isPrime = True
if n < 2:
    isPrime = False
for i in range(2, int(math.sqrt(n)) + 1):
    if (n % i == 0):
        isPrime = False
        break
if (isPrime):
    print("YES")
else:
    print("NO")