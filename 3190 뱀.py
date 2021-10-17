from collections import deque
# f= open("in.txt","r")

# n = int(f.readline())
n = int(input())
# apple_num = int(f.readline())
apple_num = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(apple_num):
    # r, c = map(int, f.readline().split())
    r,c = map(int, input().split())
    arr[r-1][c-1] = 1

# change_num = int(f.readline())
change_num = int(input())
change_lst = []

for i in range(change_num):
    # change = list(f.readline().split())
    change = list(input().split())
    change_lst.append([int(change[0]), change[1]])

dx = [-1,0,1,0]
dy = [0,1,0,-1]

dir = 1
time = 0
change_idx = 0
que = deque()
que.append((0,0))
while True:
    time+=1


    now = que.popleft()
    r = now[0] + dx[dir]
    c = now[1] + dy[dir]

    if r<0 or c<0 or r>=n or c>=n or arr[r][c] == -1 :
        print(time)
        break

    # 사과가 있을 때
    if arr[r][c] == 1:
        arr[r][c] = 0
        que.appendleft((now[0],now[1]))
        que.appendleft((r,c))

        arr[r][c] = -1
        arr[now[0]][now[1]] = -1
    #     사과가 없을 때
    else:

        que.appendleft((now[0], now[1]))
        que.appendleft((r,c))
        arr[r][c] = -1
        arr[now[0]][now[1]] = -1

        r,c = que.pop()
        arr[r][c] = 0


    if len(change_lst) > change_idx and time == change_lst[change_idx][0] :
        if change_lst[change_idx][1] == 'L':
            dir = (dir-1)%4
        else:
            dir = (dir+1)%4
        change_idx+=1


3190
