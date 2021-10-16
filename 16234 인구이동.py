from collections import deque
# f = open("in.txt")

# n, l, r = map(int, f.readline().split())
n,l,r = map(int, input().split())
arr = []

for i in range(n):
    # arr.append(list(map(int, f.readline().split())))
    arr.append(list(map(int, input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(i,j):
    global n,l,r
    que = deque()
    que.append((i,j))
    country_list = []
    sum = 0
    cnt = 0
    # 합칠 수 있는 country 탐색
    while que:
        now = que.popleft()
        i = now[0]
        j = now[1]
        country_list.append([i, j])

        sum += arr[i][j]
        cnt += 1
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]

            if x<0 or y<0 or x>=n or y>=n or V[x][y]>0 :
                continue
            diff = abs(arr[x][y] - arr[i][j])

            if diff>=l and diff<=r:
                V[x][y] = 1
                que.append((x,y))

    # 인구 합치기가 여러 나라에서 가능하면 merge_list에 더하고, 마지막에는 sum//cnt를 넣어주기
    if cnt > 1:
        country_list.append(sum//cnt)
        merge_list.append(country_list)

def change_number():
    if merge_list == []:
        return 0

    for list in merge_list:
        num = list[-1]

        for i,j in list[:-1]:
            arr[i][j] = num
    return 1

day = -1

while True:
    V = [[0 for _ in range(n)] for _ in range(n)]
    merge_list = []
    day+=1

    # 탐색하면서 국격 열기
    for i in range(n):
        for j in range(n):
            if V[i][j] == 0:
                V[i][j] = 1
                bfs(i,j)
            V[i][j] =1
    if change_number() == 0:
        break

print(day)
