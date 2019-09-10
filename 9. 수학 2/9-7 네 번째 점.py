class coordinate:
    def __init__(self, dot):
        self.x = dot[0]
        self.y = dot[1]


dot_list = list()
for _ in range(3):
    dot_list.append(coordinate(list(map(int, input().split()))))

if dot_list[0].x == dot_list[1].x:
    x = dot_list[2].x
elif dot_list[0].x == dot_list[2].x:
    x = dot_list[1].x
else:
    x = dot_list[0].x
if dot_list[0].y == dot_list[1].y:
    y = dot_list[2].y
elif dot_list[0].y == dot_list[2].y:
    y = dot_list[1].y
else:
    y = dot_list[0].y

print("%d %d" % (x, y))

