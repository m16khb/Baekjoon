num = int(input())

for _ in range(num):
    k = int(input())
    n = int(input())
    member = list()
    for i in range(1, n + 1):
        member.append(i)

    for __ in range(k):
        for i in range(1, n):
            member[i] += member[i - 1]

    print(member[-1])
