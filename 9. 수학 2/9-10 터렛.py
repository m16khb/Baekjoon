import math

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if dis == 0:
        if r1 != r2:
            print('0')
        else:
            print('-1')
    else:
        if dis == r1 + r2:
            print('1')
        elif dis < r1 + r2:
            if dis + min(r1, r2) < max(r1, r2):
                print('0')
            elif dis + min(r1, r2) == max(r1, r2):
                print('1')
            else:
                print('2')
        elif dis > r1 + r2:
            print('0')
