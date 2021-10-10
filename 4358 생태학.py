import sys

cnt = 0
dict = {}
# sys를 통해 한번에 입력 모두 받아주고 처리,,
for line in sys.stdin:
    if line == '\n':
        break

    line = line.replace("\n", "")
    if line in dict:
        dict[line] += 1
    else:
        dict[line] = 1
    cnt += 1

dict = sorted(dict.items())

for i in range(len(dict)):
    print(dict[i][0], end= " ")
    print('%.4f' %(dict[i][1]/cnt*100))
