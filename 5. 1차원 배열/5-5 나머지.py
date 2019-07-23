import collections

a = list()

for i in range(10):
    a.append(int(input()) % 42)

cnt = collections.Counter(a)
print(len(cnt))
