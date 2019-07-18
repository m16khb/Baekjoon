hour, minute = map(int, input().split())

if minute - 45 >= 0:
    print(hour, minute - 45)
elif minute - 45 < 0:
    if hour - 1 == -1:
        print(23, 60 + (minute - 45))
    else:
        print(hour - 1, 60 + (minute - 45))
