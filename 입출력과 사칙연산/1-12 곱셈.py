A = int(input())
B = int(input())

result = A * B
while B:
    print(int(B % 10) * A)
    B = int(B / 10)
print(result)
