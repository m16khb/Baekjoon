prime_num = 0
num = int(input())
candidate = list(map(int, input().split()))

for i in range(num):
    check = 0
    if candidate[i] == 1:
        continue
    if candidate[i] == 2:
        prime_num += 1
        continue
    for j in range(2, candidate[i]):
        if candidate[i] % j == 0:
            check = 1
            break
    if check == 0:
        prime_num += 1

print(prime_num)
