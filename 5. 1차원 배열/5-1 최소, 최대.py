num = int(input())

a = list(map(int, input().split()))

Max = a[0]
Min = a[0]

for i in range(num):
    if Min > a[i]:
        Min = a[i]

for i in range(num):
    if Max < a[i]:
        Max = a[i]

print(Min, Max)
