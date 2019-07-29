def hanoi(num, start, middle, end, order):
    if num == 0:
        return
    hanoi(num - 1, start, end, middle, order)
    order.append("%d %d" % (start, end))
    hanoi(num - 1, middle, start, end, order)


order = list()
hanoi(int(input()), 1, 2, 3, order)
print(len(order))
for i in range(len(order)):
    print(order[i])

