def hansu(num: int) -> int:
    if int(num / 100) == 0:
        return num
    elif int(num / 100) != 0:
        count = int()
        for i in range(100, num + 1):
            if int(i / 100) - int(i % 100 / 10) == int(i % 100 / 10) - int(i % 10):
                count += 1
        return 99 + count


print(hansu(int(input())))
