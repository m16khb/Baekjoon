num = int(input())

key = int()

for i in range(num):
    if 2 + 6 * key <= num:
        key += i
    else:
        break

if num == 1:
    print(1)
elif num == 2:
    print(2)
else:
    print(i)
