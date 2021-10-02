from collections import deque
# f = open("in.txt","r")

# n,m,gas = map(int, f.readline().split())
n,m,gas = map(int,input().split())
arr = []

i_ = [0,0,1,-1]
j_ = [1,-1,0,0]



# 각 승객에 대해서 모든 위치까지의 거리
D = [[[ 10000000 for _ in range(n)] for _ in range(n)] for _ in range(m)]
V =  [[[ 0 for _ in range(n)] for _ in range(n)] for _ in range(m)]

def bfs(p_num, si, sj):
    que = deque()
    que.append((si, sj, 0))
    D[p_num][si][sj] = 0
    while que:
        now = que.popleft()

        i = now[0]
        j = now[1]
        dist = now[2]
        for k in range(4):
            n_i = i+i_[k]
            n_j = j+j_[k]
            if n_i<0 or n_j<0 or n_i>=n or n_j>=n :
                continue
            if arr[n_i][n_j] == 0 and D[p_num][n_i][n_j] > dist+1:
                D[p_num][n_i][n_j] = dist+1
                que.append((n_i, n_j , dist+1))

# 0빈칸 , 1벽
for i in range(n):
    # 각 원소에 대해서 -1을 하고 탐색해야 한다.
    # arr.append( list(map(int,f.readline().split())))
    arr.append(list(map(int,input().split())))

# ti, tj = map(int, f.readline().split())
ti,tj = map(int,input().split())
ti -= 1
tj -= 1
mlist = []
for i in range(m):
    # mlist.append(list(map(int,f.readline().split())))
    mlist.append(list(map(int,input().split())))

# 미리 각 시작점에 대해서 모든 지점까지 거리를 찾아놓자!
for i in range(m):
    bfs(i,mlist[i][0]-1,mlist[i][1]-1)



cnt = 0
lst = [x for x in range(m)]
while cnt < m:
    cnt+=1
    min_dist = 9999999
    index = 10000000

    for i in lst:
        # min_dist = min(min_dist, D[i][ti][tj])
        if D[i][ti][tj] == min_dist:
            if mlist[index][0] == mlist[i][0] and mlist[index][1] > mlist[i][1]:
                min_dist = D[i][ti][tj]
                index = i
            if mlist[index][0] > mlist[i][0]:
                min_dist = D[i][ti][tj]
                index = i

        if D[i][ti][tj] < min_dist:
            min_dist = D[i][ti][tj]
            index = i


    if index == 10000000:
        gas = -1
        break
    # 거리 계산

    move_gas = D[index][mlist[index][2]-1][mlist[index][3]-1]

    if min_dist + move_gas  > gas:
        gas = -1
        break
    gas -= min_dist
    gas += move_gas
    lst.remove(index)
    ti = mlist[index][2]-1
    tj = mlist[index][3]-1


print(gas)
