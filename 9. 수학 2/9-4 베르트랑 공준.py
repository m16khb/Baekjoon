# 에라토스테네스의 체
n = 123456
a = [False, False] + [True]*(2 * n - 1)
primes = []

for i in range(2, 2 * n + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, 2 * n + 1, i):
            a[j] = False

while True:
    num = int(input())
    check = 0
    if num == 0:
        break
    for m in range(len(primes)):
        if num < primes[m] <= 2 * num:
            check += 1
    print(check)
