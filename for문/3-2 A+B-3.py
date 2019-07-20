num = int(input())
a = list()

for i in range(num):
    a.append(list(map(int, input().split())))

for i in range(num):
    b, c = a.pop(0)
    print("%d" % (b + c))
