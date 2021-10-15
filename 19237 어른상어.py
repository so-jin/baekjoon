# f= open("in.txt","r")

n,m,time = map(int, input().split())
# n,m,time = map(int, f.readline().split())

# 상어의 냄새 배열
arr = []

for i in range(n):
    # arr.append(list(map(int, f.readline().split())))
    arr.append(list(map(int, input().split())))
# now = list(map(int, f.readline().split()))
now = list(map(int, input().split()))
# 각 상어의 현재 방향
dir_list = [0]
dir_list+= now

# 각 상어의 방향에 대한 우선순위
dir_map = [[]]


for i in range(m):
    priority = []
    priority.append([])
    for j in range(4):
        # priority.append(list(map(int, f.readline().split())))
        priority.append(list(map(int, input().split())))
    dir_map.append(priority)
# 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽

# 1번 상어만 남으면 종료, 상어의 위치에 대한 정보
sharks = [[] for _ in range(m+1)]
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0 :
            sharks[arr[i][j]] = [i,j]
            arr[i][j] = [0, arr[i][j]]
        else:
            arr[i][j] = []


# 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽

dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]


def pri(arr):
    for i in range(len(arr)):
        print(arr[i])

now_time = 1
def put_shark(k ,d, x,y):
    global now_time
    dir_list[k] = d
    sharks[k][0] = x
    sharks[k][1] = y


def move_shark():
    global m
    global now_time
    shark_cnt = m
    while now_time <= 1000:

        # shark 만큼 돌기
        for k in range(1, m+1):

            # 해당 상어는 없는 것
            if sharks[k][0] < 0 :
                continue
            r = sharks[k][0]
            c = sharks[k][1]
            dir = dir_list[k]

            next_dir = dir_map[k][dir]

            flag = 0
            for d in next_dir:
                x = r + dx[d]
                y = c + dy[d]

                if x<0 or y<0 or x>= n or y>= n :
                    continue
                #     비어있거나 냄새가 없다면 이동
                if arr[x][y] == [] or now_time - arr[x][y][0] > time :

                    put_shark(k,d,x,y)
                    flag = 1
                    break

            # 모두 상어의 냄새가 있을 때,
            if flag == 0:
                for d in next_dir:
                    x = r+dx[d]
                    y = c+dy[d]

                    if x < 0 or y < 0 or x >= n or y >= n:
                        continue
                    #     냄새랑 자기 방향이 같을 때
                    if arr[x][y][1] == k:
                        put_shark(k,d,x,y)
                        break

        # 냄새를 저장할 때 시간 단위로 저장하기, 시간이 많이 지나면 시간 추가하기
        # 한 바퀴 돌면서 냄새 저장하기
        for k in range(1, m+1):
            if sharks[k][0] >= 0:
                # 이미 작은 번호의 상어가 있다면
                x = sharks[k][0]
                y = sharks[k][1]
                if arr[x][y] != [] and arr[x][y][0] == now_time:
                    sharks[k] = [-1,-1]
                    shark_cnt -= 1
                    if shark_cnt == 1:
                        return
                else:
                    arr[x][y] = [now_time, k]

        now_time += 1




move_shark()
if now_time == 1001:
    print(-1)
else:
    print(now_time)
