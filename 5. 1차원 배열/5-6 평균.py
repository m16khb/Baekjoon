num = int(input())
a = list(map(int, input().split()))

Max = 0

for i in range(num):
    if Max < a[i]:
        Max = a[i]

for i in range(num):
    a[i] = a[i] / Max * 100

Sum = 0

for i in range(num):
    Sum += a[i]

print(Sum / num)
