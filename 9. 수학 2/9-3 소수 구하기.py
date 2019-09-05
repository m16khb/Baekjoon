import math


def isPrime(num):
    if num == 1:
        return False
    x = int(math.sqrt(num))
    for y in range(2, x + 1):
        if num % y == 0:
            return False
    return True


# main
m, n = map(int, input().split())
for k in range(m, n + 1):
    if isPrime(k):
        print(k)
