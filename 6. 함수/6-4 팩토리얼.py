def factorial(num: int) -> int:
    if 0 <= num <= 1:
        return 1
    elif 2 <= num <= 12:
        return num * factorial(num - 1)


print(factorial(int(input())))
