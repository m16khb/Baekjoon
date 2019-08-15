num = int(input())

voca = list()

for i in range(num):
    voca.append(input())

group_voca = int()
cnt = int()

for i in voca:
    alpha = set()
    checker = 1
    for j in range(1, len(i)):
        alpha.add(i[j - 1])
        if i[j] == i[j - 1]:
            None
        elif checker == 0:
            break
        else:
            for k in list(alpha):
                if i[j] == k:
                    checker = 0
                    break
    if checker == 1:
        group_voca += 1

print(group_voca)
