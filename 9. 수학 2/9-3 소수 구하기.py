import math


def isPrime(num):
    if num == 1:
        return False
    # 소수를 구하기 위해서는 그 수의 제곱근 까지만 확인하면 됨
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
