# 최대공약수
def gcd(a, b):
    while b:
        temp = a % b
        a = b
        b = temp
    return abs(a)


# 최소공배수
def lcm(a, b):
    gcd_value = gcd(a, b)
    return abs((a * b) / gcd_value)


for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    cnt = x % (M + 1)
    tempY = x
    is_valid = False

    for __ in range(N):
        if tempY % N == 0:
            ty = N
        else:
            ty = tempY % N
        if ty == y:
            is_valid = True
            break
        cnt += M
        tempY = ty + M

    if is_valid:
        print(cnt)
    else:
        print(-1)
