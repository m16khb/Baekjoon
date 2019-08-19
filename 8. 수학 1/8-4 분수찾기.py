num = int(input())

x = int()

for i in range(num):
    if x + i < num:
        x += i
    else:
        break

if num == 1:
    print("1/1")
elif num == 2:
    print("1/2")
elif i % 2 == 0:
    print("%d/%d" % ((num - x), (i + 1) - (num - x)))
else:
    print("%d/%d" % ((i + 1) - (num - x), (num - x)))