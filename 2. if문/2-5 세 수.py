num1, num2, num3 = map(int, input().split())

if num1 < num2:
    if num2 < num3:
        print(num2)
    else:
        if num1 > num3:
            print(num1)
        else:
            print(num3)
else:
    if num1 < num3:
        print(num1)
    else:
        if num2 > num3:
            print(num2)
        else:
            print(num3)
