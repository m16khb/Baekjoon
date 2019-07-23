num = int(input())

OX = list()

for i in range(num):
    OX.append(input())

for i in range(num):
    score = 0
    sum_score = 0
    for j in range(len(OX[i])):
        if OX[i][j] == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
            sum_score += score
    print(sum_score)