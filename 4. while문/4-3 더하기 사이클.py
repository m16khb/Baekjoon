num = int(input())

N = 0
X = num

while True:
    N += 1
    X = (X % 10 * 10) + ((int(X / 10) + X % 10) % 10)
    if num == X:
        print(N)
        break
