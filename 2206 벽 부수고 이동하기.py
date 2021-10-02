from collections import deque
# f = open("in.txt","r")
# n,m = map(int,f.readline().split())
n,m = map(int, input().split())
arr = []
for i in range(n):
    # arr.append(list( f.readline().replace("\n",'')))
    arr.append(list(input().replace('\n','')))

D = [[[10000000 for _ in range(m)] for _ in range(n)] for _ in range(2)]


# D 0은 벽 깬 적 없을 때,
# D 1은 벽 깬 적 있을 때,
#start는 0,0 end는 n,m
dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs():
    que = deque()
    que.append([0,0])
    D[0][0][0] = 1
    D[1][0][0] = 1
    while que :
        now = que.popleft()

        i = now[0]
        j = now[1]
        # 벽이라면
        if i == m-1 and j == n-1:
            return
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]

            if ni<0 or nj<0 or ni>=n or nj>=m:
                continue
            if arr[ni][nj] == '1':
                # 벽에 대해서 최솟값 
                if D[1][ni][nj] > D[0][i][j] + 1:
                    D[1][ni][nj] = D[0][i][j] + 1
                    que.append([ni,nj])
            # 벽이 아니라면
            else:
                min_dist = min(D[1][i][j], D[0][i][j])
                flag = 0
                # 지금까지 벽이 없었을 때의 최솟값 
                if D[0][ni][nj] > D[0][i][j] + 1:
                    D[0][ni][nj] = D[0][i][j] + 1
                    flag = 1
                # 지금까지 벽이 있었을 때의 최솟값 
                if D[1][ni][nj] > min_dist + 1:
                    D[1][ni][nj] = min_dist + 1
                    flag = 1
                # 최솟값이 갱신되었을 때, que에 넣어준다. 
                if flag == 1:
                    que.append([ni,nj])


bfs()
# 벽이 있을 때와 없을 때 중 최솟값 구하기 
dist = min(D[1][n-1][m-1], D[0][n-1][m-1])

if dist == 10000000:
    print(-1)
else:
    print(dist)
