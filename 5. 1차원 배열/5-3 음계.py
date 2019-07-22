ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = list()
descending += ascending
descending.reverse()

a = list(map(int, input().split()))

if a == ascending:
    print("ascending")
elif a == descending:
    print("descending")
else:
    print("mixed")
