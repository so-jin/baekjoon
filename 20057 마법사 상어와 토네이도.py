# f = open("in.txt", "r")

# size = int(f.readline())
size = int(input())
m = []
for i in range(size):
    # m.append(list(map(int, f.readline().split())))
    m.append(list(map(int,input().split())))


# 시작은 정중앙
# 모두 밖에 나가면 끝내버리기

# 밖으로 나간 모래 양
out = 0

i = size//2
j = size//2

i_ = [0,1,0,-1]
j_ = [-1,0,1,0]

dir = -1
flag = 0
dir_len = 0
ret = 0

def pri(arr):
    for i in range(len(arr)):
        print(arr[i])

def move(i, j , sand):
    # 판을 넘어가면 sand를 return
    if i<0 or j<0 or i>=size or j>=size:
        return sand
    m[i][j] += sand
    return 0


def wind(i,j,dir, u,d):
    global ret
    # y자리의 모래의 양
    sand = m[i][j]

    # x자리로 복귀 , 0.01
    i -= i_[dir]
    j -= j_[dir]
    ret += move(i + i_[u], j + j_[u], sand // 100)
    ret += move(i + i_[d], j + j_[d], sand // 100)

    # y자리에 대해서 0.07, 0.02
    i += i_[dir]
    j += j_[dir]

    ret += move(i+i_[u], j+j_[u], int(sand*0.07))
    ret += move(i+i_[u]*2, j+j_[u]*2, int(sand*0.02))
    ret += move(i + i_[d], j + j_[d], int(sand * 0.07))
    ret += move(i + i_[d] * 2, j + j_[d] * 2, int(sand * 0.02))

    #  a자리에 대해서 0.1
    i += i_[dir]
    j += j_[dir]

    ret += move(i+i_[u], j+j_[u], sand //10)
    ret += move(i + i_[d], j + j_[d], sand // 10)

    # a 다음 자리에 대해서 0.05
    i += i_[dir]
    j += j_[dir]
    ret += move(i , j , sand // 20 )

while True:
    # 판을 다 돌면 break
    if i<0 or j<0 :
        break

    if flag == 0:
        # 바람이 한 방향으로 가는 길이 증가 (같은 길이로 2번 간 뒤)
        dir_len += 1
        flag = 1
    else:
        flag = 0

    # 바람 방향 변경
    dir = (dir+1)%4
    for k in range(dir_len):
        i += i_[dir]
        j += j_[dir]

        # y의 위치에 모래가 없으면
        if m[i][j] == 0:
            continue
        # 위, 아래의 방향
        u = (dir+3)%4
        d = (dir+1)%4
        sand = m[i][j]

        wind(i,j,dir,u,d)

        # 남아서 a에 추가되어야 할 모래의 양
        a =  sand - (sand//10)*2 - (sand//100)*2 - int(sand*0.07)*2 - int(sand*0.05) - (sand//50)*2
        ret += move(i+i_[dir],j+j_[dir], a)

        # y의 모래는 0으로 변경
        m[i][j] = 0


print(ret)
