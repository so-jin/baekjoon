import copy
from collections import deque
# f = open("in.txt","r" )

# n, query_num = map(int, f.readline().split())

n,query_num = map(int, input().split())
# print()
arr = []
size = 2**n
for i in range(2**n):
    # arr.append(list(map(int, f.readline().split())))
    arr.append(list(map(int, input().split())))

# queries = list(map(int, f.readline().split()))
queries = list(map(int, input().split()))
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 주변의 얼음 갯수 세기
def count_ice(i,j):
    global size
    cnt = 0
    for k in range(4):
        next_i = i+dx[k]
        next_j = j+dy[k]
        if next_i<0 or next_j<0 or next_i>= size or next_j>=size or arr[next_i][next_j] == 0:
            continue
        cnt += 1
    return cnt

# 반시계방향 회전
def change_dir(tmp_arr, r,c):
    n = len(tmp_arr)
    for i in range(n):
        for j in range(n):
            arr[j+r][n-1-i+c] = tmp_arr[i][j]

# size만큼 반시계방항 회전
def change(size):
    global arr
    # 두 개로 나눠서 하기
    # (0,0)에서 시작하는 것
    for i in range(0, 2**n , size):
        for j in range(0,2**n, size):
            tmp_arr = []
            for l in range(i,i+size):
                tmp_arr.append(arr[l][j:j+size])
            change_dir(tmp_arr, i,j)

# 주변에 얼음이 3개 이하이면 얼음 녹음
def minus_ice():
    global arr
    global size
    new_arr = copy.deepcopy(arr)

    for i in range(size):
        for j in range(size):
            if count_ice(i,j) < 3 and arr[i][j] >0:
                new_arr[i][j] -= 1

    arr = new_arr

# bfs로 최대 그룹 찾기
def find_iceblock():
    V = [[0 for _ in range(size)] for _ in range(size)]
    max_cnt = 0
    for i in range(size):
        for j in range(size):
            # 여기서부터 그룹 찾기
            if V[i][j] == 0 and arr[i][j] >0:
                que = deque()
                que.append((i,j))
                V[i][j] = 1
                cnt = 0
                while que:
                    now = que.popleft()
                    cnt += 1
                    for k in range(4):
                        next_i = now[0] + dx[k]
                        next_j = now[1] + dy[k]

                        if next_i<0 or next_j<0 or next_i>=size or next_j>=size:
                            continue

                        if V[next_i][next_j] == 0 and arr[next_i][next_j] > 0 :
                            V[next_i][next_j] = 1
                            que.append((next_i, next_j))

                max_cnt = max(max_cnt, cnt)
    return max_cnt


for query in queries:

    change(2**query)
    minus_ice()


result = 0
for i in range(2**n):
    for j in range(2**n):
        result += arr[i][j]

print(result)
print(find_iceblock())
# dfs로 얼음 그룹 찾기


