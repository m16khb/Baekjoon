num = int(input())
a = list()

for i in range(num):
    a.append(list(map(int, input().split())))

for i in range(1, num + 1):
    b, c = a.pop(0)
    print("Case #%d: %d" % (i, b + c))
