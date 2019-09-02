num1 = int(input())
num2 = int(input())
prime_num = list()

for i in range(num1, num2 + 1):
    check = 0
    if i == 1:
        continue
    if i == 2:
        prime_num.append(i)
        continue
    for j in range(2, i):
        if i % j == 0:
            check = 1
            break
    if check == 0:
        prime_num.append(i)

SUM = 0

if not prime_num:
    print('-1')
else:
    for i in range(len(prime_num)):
        SUM += prime_num[i]
    print(SUM)
    print(prime_num[0])
