num = int(input())

if num % 5 == 0:
    print(num//5)
elif (num % 5) % 3 == 0:
    print(num // 5 + (num % 5) // 3)
else:
    check = 0
    for i in range(int(num / 5), -1, -1):
        if((num - 5 * i) % 3) == 0:
            print(i + (num - 5 * i) // 3)
            check = 1
            break
    if check == 0:
        print(-1)
