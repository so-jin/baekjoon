from collections import deque
# f = open("in.txt")
#  제자리 상 우 하 좌
dx = [0,-1,0,1,0]
dy = [0,0,1,0,-1]

# y,x,dist,power

# test_num = int(f.readline())
test_num = int(input())
result = 0
def pri(arr):
    for i in range(len(arr)):
        print(arr[i])
# bfs
def mark(r,c, idx, dist):
    que = deque()
    que.append((r,c,1))
    arr[r][c].append(idx)
    V = [[0 for _ in range(11)] for _ in range(11)]
    V[r][c] = 1
    while que:
        now = que.popleft()
        i = now[0]
        j = now[1]
        now_dist = now[2]
        for k in range(1,5):
            x = i+dx[k]
            y = j+dy[k]
            if x<=0 or y<=0 or x>10 or y>10 or V[x][y] == 1:
                continue

            V[x][y] = 1
            arr[x][y].append(idx)

            if now_dist < dist:
                que.append((x,y,now_dist+1))
def move(a, dir):
    a[0] = a[0]+dx[dir]
    a[1] = a[1]+dy[dir]

def get(a_charge):
    if a_charge != []:
        return charges[a_charge[0]][3]
    return 0
def compare(a,b):
    if a[0] == b[0]:
        return False
    return True

for t in range(test_num):
    # time, charge_num = map(int, f.readline().split())
    # move_a = list(map(int, f.readline().split()))
    # move_b = list(map(int, f.readline().split()))
    time, charge_num = map(int, input().split())
    move_a = list(map(int, input().split()))
    move_b = list(map(int, input().split()))

    arr = [[[] for _ in range(11)] for _ in range(11)]
    people = [[[] for _ in range(11)] for _ in range(11)]
    result = 0
    a = [1,1]
    b = [10,10]
    charges = []
    for i in range(charge_num):
         # charges.append(list(map(int,f.readline().split())))
        charges.append(list(map(int, input().split())))
    charges.sort(key = lambda x : x[3], reverse=True)

    # def로 가면서 배열에 표시
    for i in range(len(charges)):
        charge = charges[i]
        mark(charge[1], charge[0], i, charge[2])

    # pri(arr)

    for k in range(time+1):
        a_charge = arr[a[0]][a[1]]
        b_charge = arr[b[0]][b[1]]

        #  두 충전기가 겹치는게 없으면 !!
        if a_charge == [] or b_charge == [] or compare(a_charge,b_charge):
            result+= get(a_charge)
            result+= get(b_charge)
        # 가장 충전 잘 되는 충전기 같을 때
        elif len(a_charge) == 1 :
            result += get(a_charge)
            result += get(b_charge[1:])
        elif len(b_charge) == 1:
            result += get(b_charge)
            result += get(a_charge[1:])

        #  두 충전기가 겹친다면 가장 효율적인 방법으로 충전
        else:
        #     한 충전기를 동시에 사용할 지, 다른 충전기를 사용할 지 비교
            # 한 충전기만 사용
            # a_win = charges[a_charge[0]][3]+ charges[b_charge[1]][3]
            # b_win = charges[a_charge[1]][3] + charges[b_charge[0]][3]
            a_win = get(a_charge) + get(b_charge[1:])
            b_win = get(a_charge[1:]) + get(b_charge)
            result += max(a_win, b_win)

        # 사용자 위치 이동
        if k != time:
            move(a, move_a[k])
            move(b, move_b[k])



    print("#"+str(t+1), result)

    # break
