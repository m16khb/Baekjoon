croatia_alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

voca = input()

for i in croatia_alpha:
    voca = voca.replace(i, '*')

print(len(voca))
