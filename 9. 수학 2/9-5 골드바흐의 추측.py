# 에라토스테네스의 체
n = 10000
a = [False, False] + [True]*(2 * n - 1)
primes = []

for i in range(2, 2 * n + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, 2 * n + 1, i):
            a[j] = False

for _ in range(int(input())):
    num = int(input())
    candidate = 0
    for i in range(len(primes)):
        if num / 2 <= primes[i]:
            candidate = i
            break
    if primes[candidate] + primes[candidate] == num:
        print("%d %d" % (primes[candidate], primes[candidate]))
    elif primes[candidate] + primes[candidate] > num:
        check = 0
        for n in range(candidate):
            if check == 1:
                break
            for m in range(candidate):
                if primes[candidate - m] + primes[candidate + n] == num:
                    print("%d %d" % (primes[candidate - m], primes[candidate + n]))
                    check = 1
                    break
