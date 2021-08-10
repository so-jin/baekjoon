from collections import deque

# f = open("babyshark.txt", 'r')

# size = int(f.readline())
size = int(input())
arr = []
for i in range(size):
    # line = f.readline()
    line = input()
    arr.append( list(map(int, line.split())) )
    # print(arr)

node = ()
eat_cnt = 0
for i in range(size):
    for j in range(size):
        if arr[i][j] == 9:
            shark = (i,j,2)
            # print(shark)
            arr[i][j] = 0

x_ = [0,0,-1,1]
y_ = [1,-1,0,0]


def bfs():
    global size
    fish = (20, 20 ,400)
    dist = 0
    queue = deque([(shark[0],shark[1],0)])
    visit = [[ 0 for _ in range(size)] for _ in range(size)]
    #print(visit)
    while queue :
        now = queue.popleft()
        #print('now',now)
        if now[2] + 1 > fish[2] :
            queue.clear()
            break

        # distance 가 더 작으면 queue에 넣기
        else:
            for i in range(4):
                x = now[0]+x_[i]
                y = now[1]+y_[i]
                dist = now[2]
                if x < 0 or x >= size or y < 0 or y >= size or visit[x][y] == 1:
                    continue
                ## dist 조건 추가 가
                visit[x][y] = 1
                if arr[x][y] == shark[2] or arr[x][y]==0:
                    if dist+1 < fish[2] :
                        queue.append((x,y,dist+1))
                    #print('possible to move', x, y, arr[x][y])

                ## possible to eat and shortest distance
                elif arr[x][y] < shark[2] :
                    #print('possible to eat', x,y,arr[x][y])
                    ## 거리 짧을 때 update
                    if dist + 1 < fish[2] :
                        fish = (x, y ,dist+1)
                    ## 거리 같으면 비교한다
                    elif dist + 1 == fish[2]:
                        if fish[0] > x :
                            fish = (x, y , dist+1 )
                        elif fish[0] == x and fish[1] > y:
                            fish = (x, y , dist+1)

    #print('fish', fish)
    return fish


time = 0
cnt = 0
s_size = 2
while True :
    fish = bfs()
    if fish[0] == 20:
        break
    time += fish[2]

    cnt += 1
    if cnt == s_size :
        s_size+= 1
        cnt = 0
    shark = (fish[0], fish[1], s_size)
    # print('eat', shark)
    arr[fish[0]][fish[1]] = 0


print(time)



# f.close()

