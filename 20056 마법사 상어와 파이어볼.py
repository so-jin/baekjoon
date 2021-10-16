# f = open("in.txt")


# n, ball_num, move = map(int, f.readline().split() )
n, ball_num , move = map(int, input().split())
arr = [ [[] for _ in range(n)] for _ in range(n)]
balls = []


for i in range(ball_num):
    # r,c,m,s,d = map(int, f.readline().split())
    r,c,m,s,d = map(int, input().split())
    balls.append([r-1,c-1,m,s,d])


dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]


# 모든 파이어볼 이동

def pri(arr):
    for i in range(len(arr)):
        print(arr[i])

def check_dir(fireballs):
    idx = fireballs[0]
    dir = balls[idx][4] % 2

    for i in range(1, len(fireballs)):
        idx = fireballs[i]
        if dir != balls[idx][4]%2:
            return 1
    return 0

for cnt in range(move):
    arr = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(len(balls)):
        ball = balls[i]
        d = ball[4]
        s = ball[3]
        x = (ball[0] + dx[d] * s) % n
        y = (ball[1] + dy[d] * s) % n

        arr[x][y].append(i)

    new_balls = []

    for i in range(n):
        for j in range(n):
            # 공이 2개 이상 존재하면 4개의 공으로 나누기 
            if len(arr[i][j])>=2:
                fireballs = arr[i][j]

                m = 0
                s = 0
                for k in range(len(fireballs)):
                    idx = fireballs[k]
                    m += balls[idx][2]
                    s += balls[idx][3]

                m //= 5
                s //= len(fireballs)

                # 질량이 0이하이면 버리기 
                if m> 0:
                    dir = check_dir(fireballs)
                    for k in range(4):
                        new_balls.append([i,j,m,s,dir])
                        dir+=2
            # 그냥 공이 1개 존재하면
            elif len(arr[i][j])>0:
                k = arr[i][j][0]
                new_balls.append([i,j, balls[k][2], balls[k][3], balls[k][4]])

    balls = new_balls


result = 0
for i in balls:
    result += i[2]

print(result)
