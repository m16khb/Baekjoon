al_dic = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
          'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

voca = list(input().upper())

max_dic_list = list()

for i in voca:
    al_dic[i] += 1

for key, value in al_dic.items():
    if value == max(al_dic.values()):
        max_dic_list.append(key)

if len(max_dic_list) >= 2:
    print('?')
else:
    print(max_dic_list.pop())
