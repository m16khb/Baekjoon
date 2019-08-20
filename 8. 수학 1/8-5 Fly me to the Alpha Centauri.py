num = int(input())
data = list()
distance = list()
result = list()

for i in range(num):
    data.append(list(map(int, input().split())))

for i in range(len(data)):
    distance.append(data[i][1] - data[i][0])

for i in range(len(distance)):
    result.append(int(distance[i] ** 0.5))

for i in range(len(result)):
    if distance[i] <= 3:
        result[i] = distance[i]
    elif distance[i] <= result[i] ** 2:
        Sum = int()
        for j in range(result[i] + 1):
            Sum += j
        result[i] = j * 2 - 1
    elif distance[i] <= result[i] ** 2 + result[i]:
        Sum = int()
        for j in range(result[i] + 1):
            Sum += j
        result[i] = j * 2
    else:
        Sum = int()
        for j in range(result[i] + 1):
            Sum += j
        result[i] = j * 2 + 1

for i in range(len(result)):
    print(result[i])
