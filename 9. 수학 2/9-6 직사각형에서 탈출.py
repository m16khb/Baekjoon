class distance:
    def __init__(self, x, y, w, h):
        if w - x < x:
            self.m = w - x
        else:
            self.m = x
        if h - y < y:
            self.n = h - y
        else:
            self.n = y

    def check(self):
        if self.m >= self.n:
            return self.n
        else:
            return self.m


x, y, w, h = map(int, input().split())
dis = distance(x, y, w, h)

print(dis.check())

