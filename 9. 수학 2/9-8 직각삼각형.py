while True:
    num1, num2, num3 = map(int, input().split())
    if num1 == 0 and num2 == 0 and num3 == 0:
        break
    num = [num1, num2, num3]
    temp = max(num)
    num.remove(max(num))
    if temp * temp == (num[0] * num[0]) + (num[1] * num[1]):
        print("right")
    else:
        print("wrong")
