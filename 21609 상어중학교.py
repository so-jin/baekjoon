from collections import deque
# f = open("in.txt")

# n,m = map(int,f.readline().split())
n,m = map(int, input().split())
arr = []
for i in range(n):
    # arr.append(list(map(int, f.readline().split())))
    arr.append(list(map(int, input().split())))


dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 반시계 회전
# 중력 작용
def pri(arr):
    for i in range(len(arr)):
        print(arr[i])

def del_maxblock(i,j,color):
    que = deque()
    que.append((i,j))
    V = [[0 for _ in range(n)] for _ in range(n)]
    V[i][j] = 1
    arr[i][j] = -2
    while que:
        now = que.popleft()
        i = now[0]
        j = now[1]
        for k in range(4):
            i_ = i+dx[k]
            j_ = j+dy[k]
            if i_<0 or j_<0 or i_>=n or j_>=n or V[i_][j_] == 1:
                continue
            if arr[i_][j_] == color or arr[i_][j_] == 0:
                que.append((i_,j_))
                V[i_][j_] = 1
                arr[i_][j_] = -2



def find_bigblock():
    # 색 별로 탐색...
    max_block = 0
    max_rain = 0
    index = 0
    # 각 색별로 탐색
    for c in range(1, m+1):
        # 색 별로 visit배열을 따로 둔다.
        V = [[0 for _ in range(n)] for _ in range(n)]

        # 모든 범위에 대해서 탐색
        for i in range(n):
            for j in range(n):
                if arr[i][j] == c and V[i][j] == 0:
#                      bfs로 가면서 탐색한다.
#                       block의 최대 크기를 파악
                    que = deque()
                    que.append((i,j))
                    V[i][j] = 1
                    cnt = 0
                    rcnt = 0
                    while que:
                        now = que.popleft()
                        ni = now[0]
                        nj = now[1]
                        cnt+=1
                        # 무지개 블록 갯수 따로 세기
                        if arr[ni][nj] == 0:
                            rcnt +=1

                        for k in range(4):
                            i_ = ni + dx[k]
                            j_ = nj + dy[k]
                            if i_<0 or j_<0 or i_>=n or j_>=n or V[i_][j_] == 1:
                                continue
                            #     색이 있거나 무지개이면 추가
                            if arr[i_][j_] == c or arr[i_][j_] == 0:
                                que.append((i_, j_))
                                V[i_][j_] = 1

                    # max block의 크기가 같으면 rain block이 더 많은 것 찾기
                    if cnt>1 and max_block == cnt:
                        if max_rain < rcnt :
                            max_rain = rcnt
                            index = (i,j,c)

                        # rain block도 같다면, 행이 큰 것을, 행도 같다면 열의 큰 것을 고르기
                        elif max_rain == rcnt:
                            if index[0] == i and index[1] < j:
                                index = (i,j,c)
                            elif index[0] < i:
                                index = (i,j,c)

                    elif max_block < cnt :
                        max_block = cnt
                        max_rain = rcnt
                        index = (i,j, c)

    if max_block >= 2:
        del_maxblock(index[0],index[1],index[2])
        return max_block*max_block
    else:
        return 0

score=0
# 중력 작용

# 중력 작용했을 때 밀기,
def gravity():
#     열 별로 중력 작용
    G = [[[] for _ in range(n)] for _ in range(n)]

    for j in range(n):
        i = n-1
        index = n-1
        while i>=0:
            if arr[i][j] == -1:
                index = i
                G[j][index].append(arr[i][j])

            elif arr[i][j] != -2:
                G[j][index].append(arr[i][j])

            i-=1

    for i in range(n):
        for j in range(n):
            arr[i][j] = -2

#     배열 변경
    for j in range(n):
        i = n-1
        while i>=0:
            if G[j][i] != []:
                index = i
                for k in G[j][i] :
                    arr[index][j] = k
                    index -= 1
            i-=1


# 배열 회전 / 반시계방
def change_dir():
    n_arr = [ [0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            n_arr[n-1-j][i] = arr[i][j]

    return n_arr



# 오토 플레이

result = 0
while True:
    # 가장 큰 그룹 찾아서 제거

    score = find_bigblock()
    if score <2:
        break
    result += score
    # 격자에 중력 작용
    gravity()

    # 격자가 90도 반시계 방향으로 회전
    arr = change_dir()

    gravity()

print(result)
