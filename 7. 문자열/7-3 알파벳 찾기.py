String = input()

use = list()

for i in range(26):
    use.append(int(-1))

for i in range(len(String)):
    if use[ord(String[i]) - 97] == -1:
        use[ord(String[i]) - 97] = i

for i in range(len(use)):
    print(use[i], end=' ')
