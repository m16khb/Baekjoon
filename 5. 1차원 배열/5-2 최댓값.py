a = list()

for i in range(9):
    a.append(int(input()))

Max = 0
index = 0

for i in range(9):
    if Max < a[i]:
        Max = a[i]
        index = i + 1

print("%d\n%d" % (Max, index))
