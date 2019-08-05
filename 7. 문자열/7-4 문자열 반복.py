Iter = int(input())

for i in range(Iter):
    R, S = map(str, input().split())
    R = int(R)
    P = str()

    for j in range(len(S)):
        print(R*S[j], end='')
    print()
