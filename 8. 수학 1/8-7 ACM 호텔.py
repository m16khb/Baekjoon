num = int(input())
A = list()

for i in range(num):
    H, W, N = map(int, input().split())
    A.append(str("%d%02d" % ((N - 1) % H + 1, (N - 1) // H + 1)))

for i in range(len(A)):
    print(A[i])