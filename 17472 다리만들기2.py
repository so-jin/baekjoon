# f = open("in.txt","r")

# test_num = int(f.readline())
test_num = int(input())
# 상 하 좌 우
#
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def chage_dir(dir):
    if dir == 0 or dir == 2:
        return dir+1
    else:
        return dir-1
result = 0
def move():
    global dic
    global result
    time = 1
    # 0.5를 먼저 생각 그리고 1초를 생각
    del_lst = []
    for t in dic:
        i = t[0]
        j = t[1]
        num = dic[t][0]
        dir = dir_lst[num][0]

        x = i+dx[dir]
        y = j+dy[dir]

        # 부딪힐 때
        if (x,y) in dic and (x,y) not in del_lst:
            nex_idx = dic[(x,y)][0]
            # 방향이 정 반대 원자 폭발
            if chage_dir(dir_lst[nex_idx][0]) == dir:
                result = result + dir_lst[nex_idx][1] + dir_lst[num][1]
                # 파괴되고 더하기
                del_lst.append(t)
                del_lst.append((x,y))


    for item in del_lst:
        del dic[item]

    new_dic = {}
    del_lst = []
    # 1초 단위로
    for t in dic:
        i = t[0]
        j = t[1]
        num = dic[t][0]
        dir = dir_lst[num][0]

        x = i+dx[dir]
        y = j+dy[dir]

        if (x,y) in new_dic:
            new_dic[(x,y)].append(num)

        else:
            new_dic[(x,y)] = [num]

    dic = new_dic
    for t in dic:
        if len(dic[t]) > 1:
            crash_lst = dic[t]
            for item in crash_lst:
                result += dir_lst[item][1]
            del_lst.append(t)

    for item in del_lst:
        del dic[item]



for t in range(test_num):
    # cnt = int(f.readline())
    cnt = int(input())
    energy_sum = 0
    dic = {}
    dir_lst = []
    for k in range(cnt):
        result = 0
        x,y,dir,energy = map(int, input().split())

        energy_sum += energy
        dic[(y,x)] = [k]
        dir_lst.append([dir, energy])

    for c in range(1000):
        move()
    print("#"+str(t+1),result)


