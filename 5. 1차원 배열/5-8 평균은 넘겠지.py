num = int(input())

student = list()

for i in range(num):
    student.append(list(map(int, input().split())))

for i in range(num):
    sum_score = 0
    good = 0
    for j in range(1, student[i][0] + 1):
        sum_score += student[i][j]
    average = sum_score / student[i][0]
    for j in range(1, student[i][0] + 1):
        if student[i][j] > average:
            good += 1
    print("%.3f%%" % (good / student[i][0] * 100))
