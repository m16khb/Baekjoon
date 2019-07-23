num1 = int(input())
num2 = int(input())
num3 = int(input())

num4 = num1 * num2 * num3

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while num4 != 0:
    a[num4 % 10] += 1
    num4 = int(num4 / 10)

for i in range(len(a)):
    print(a[i])
