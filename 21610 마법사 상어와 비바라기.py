# f = open("in.txt")

# n,m = map(int, f.readline().split())
n, m = map(int, input().split())

arr = []

for i in range(n):
    # arr.append(list(map(int, f.readline().split())))
    arr.append(list(map(int, input().split())))

move = []
for i in range(m):
    # move.append(list(map(int, f.readline().split())))
    move.append(list(map(int, input().split())))

cloud = [[0 for _ in range(n)] for _ in range(n)]

cloud[n-2][0] = 1
cloud[n-1][1] = 1
cloud[n-2][1] = 1
cloud[n-1][0] = 1

di = [0,0,-1,-1,-1,0,1,1,1]
dj = [0,-1,-1,0,1,1,1,0,-1]

dx = [-1,-1,1,1]
dy = [-1,1,-1,1]

def pri(arr):
    for i in range(n):
        print(arr[i])

def duplicate(i,j):
    cnt = 0
    for k in range(4):
        i_ = i+dx[k]
        j_ = j+dy[k]
        if i_<0 or j_<0 or i_>=n or j_>=n:
            continue
        if arr[i_][j_] > 0:
            cnt+=1
    return cnt

def play(k):
    global cloud
    dir = move[k][0]
    dist = move[k][1]

    n_cloud = [[0 for _ in range(n)] for _ in range(n)]

    # cloud 이동  
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1:
                i_ = (i+di[dir]*dist)%n
                j_ = (j+dj[dir]*dist)%n
                arr[i_][j_] += 1
                n_cloud[i_][j_] = 1

    # 물 복사 
    for i in range(n):
        for j in range(n):
            if n_cloud[i][j] == 1:
                arr[i][j] += duplicate(i,j)

    # 구름 생성 
    cloud = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if n_cloud[i][j] == 0 and arr[i][j] >= 2:
                arr[i][j] -= 2
                cloud[i][j] = 1



# 명령만큼 play 
for i in range(m):
    play(i)

result = 0
for i in range(n):
    for j in range(n):
        result += arr[i][j]

print(result)
