def factorial(num: int) -> int:
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(int(input())))
