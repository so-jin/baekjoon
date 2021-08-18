# f = open("babyshark.txt", 'r')

arr = [[] for _ in range(4)]
ex = [ True for _ in range(17)]
for i in range(4):
    # line = f.readline().split()
    line = input().split()
    line = list(map(int,line))

    for j in range(0,8,2):
        arr[i].append((line[j],line[j+1]-1))
    arr.append(line)


for i in range(4):
    for j in range(4):
        now = arr[i][j]
        ex[now[0]] = (i,j)


def pri(arr):
    for i in range(4):
        print(arr[i])

answer = 0

# 방향 이동
i_ = [-1,-1,0,1,1,1,0,-1]
j_ = [0,-1,-1,-1,0,1,1,1]

## 상어가 있거나 경계면 이동 불가능 상어 -1
def movable(arr, r,c, dir):
    r = r+i_[dir]
    c = c+j_[dir]

    # 경계를 넘어갔거나 상어를 만났을 때
    if r<0 or c<0 or r>=4 or c>=4 or arr[r][c][0] == 0:
        return False
    return True

def fish_move(arr, ex):

    for i in range(1,17):
        # print('to move',i)
        # pri()
        if ex[i] == False:
            continue
        r = ex[i][0]
        c = ex[i][1]

        dir = arr[r][c][1]
        #이동할 수 없으면 이동할 수 있을때까지 확인

        # 이동 가능하다면 그 방향으로 이동
        ## 이동이 모두 불가능한 경우는 생각하지 않았음.
        # 고려해야할까?
        while True:
            result = movable(arr, r,c,dir)
            if result == True:
                break
            dir = ( dir+ 1) % 8


        # 이동 가능한 방향 찾았으면, 그 방향으로 이동 (물고기 서로 바꾸기)
        ni = r + i_[dir]
        nj = c + j_[dir]

        # 빈 칸이면 현재 물고기만 이동하고, 기록
        if arr[ni][nj][0] == -1:
            arr[ni][nj] = (i, dir)
            ex[arr[ni][nj][0]] = (ni,nj)
            arr[r][c] = (-1,-1)

        else:
            # 물고기 서로 이동
            next = arr[ni][nj]
            arr[ni][nj] = (i, dir)
            arr[r][c] = next

            # 물고기 위치 기록 변경
            ex[arr[ni][nj][0]] = (ni, nj)
            ex[arr[r][c][0]] = (r,c)



        # 절대 이동할 수 없으면??


def dfs(fish, nex, sum):
    global answer
    shark = nex[0]
    dir = fish[shark[0]][shark[1]][1]
    i = shark[0] + i_[dir]
    j = shark[1] + j_[dir]
    ## 가능한 모든 경로에 대해 dfs 탐색 수행
    ## 가능한 모든 경로로 가보기

    while i>=0 and j>=0 and i<4 and j<4:
        ## 물고기가 존재한다면 먹고 dfs

        if fish[i][j][0] >=1 and fish[i][j][0] <= 16 :
            nex_ = []
            fish_= [ [ 0 for _ in range(4)] for _ in range(4)]
            for k in range(17):
                nex_.append(nex[k])
            for m in range(4):
                for n in range(4):
                    fish_[m][n] = fish[m][n]
            #물고기 잡아먹고, 상어는 그 방향을 가진다.
            food = fish_[i][j]
            fish_[i][j] = (0, food[1])
            # 원래 상어의 위치는 빈 공간
            fish_[shark[0]][shark[1]] = (-1,-1)

            # 서로 자신의 위치 정보 update
            nex_[food[0]] = False
            nex_[0] = (i,j)

            fish_move(fish_,nex_)

            dfs(fish_, nex_, sum+food[0])

        i = i + i_[dir]
        j = j + j_[dir]
        # pri(fish_)
        # print(nex_)
    answer = max(answer, sum)


def play():
    sum = 0
    # 처음에 0,0들어가서 먹는다.
    # 먹은 상어 더하기
    sum += arr[0][0][0]
    # 먹은 자리에 상어가 이동, 상어는 0번 방향은 물고기의 방향을 유지
    # 빈칸은 -1
    ex[arr[0][0][0]] = False
    ex[0] = (0,0)
    arr[0][0] = (0, arr[0][0][1])

    ## 물고기 이동하고 , 상어가 먹는다. 반복
    fish = [[0 for _ in range(4)] for _ in range(4)]
    nex = []
    for m in range(4):
        for n in range(4):
            fish[m][n] = arr[m][n]
    for i in range(17):
        nex.append(ex[i])
    fish_move(fish, nex)

    dfs(fish, nex, sum)




play()
# pri()
print(answer)

