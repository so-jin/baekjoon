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
        # if x>2000 or y>2000 or x<-2000 or y<-2000:
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

    if len(dic) == 1:
        return True
    return False

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
        dic[(y*2,x*2)] = [k]
        dir_lst.append([dir, energy])

    for c in range(2000):
        if move() :
            break
    print("#"+str(t+1),result)


