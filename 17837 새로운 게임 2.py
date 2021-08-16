# f = open("babyshark.txt", 'r')

# n, k = f.readline().split()
n, k = input().split()
# r, c, num = input().split()
n = int(n)
k = int(k)

arr = []
map = [[[] for _ in range(n)] for _ in range(n)]

## 말에 대한 정보 배열
horse = [ [] for _ in range(k+1)]
# 입력 및 초기
for i in range(n):
    # line = f.readline()
    line = input()
    line = list(line.split())
    arr.append(line)


for i in range(k):
    # r, c, dir = f.readline().split()
    r,c,dir = input().split()
    r = int(r)-1
    c = int(c)-1
    dir = int(dir)
    map[r][c].append((i+1, dir))
    horse[i+1] = (r,c)

#print 함수
def pri(arr):
    for i in range(n):
        print(arr[i])


# 말을 방향에 따라서 이동,
# 데려갈 친구들 있으면 배열로서 함꼐 가져가기
# 이동한 곳에서 append로 붙여버리기
# Red일 경우 순서 바꿔야 함

i_ = [0,0,0,-1,1]
j_ = [0,1,-1,0,0]

def change_dir(dir):
    if dir == 1:
        return 2
    elif dir == 2:
        return 1
    elif dir == 3:
        return 4
    else:
        return 3

# now = (index, dir)
def move(bi, bj ,now, left):
    index = now[0]
    dir = now[1]
    i = bi+i_[dir]
    j = bj+j_[dir]

    ## 같이 이동할 아이들이 있을 때는 추가적인 처리 필요
    if i<0 or j<0 or i>=n or j>=n or arr[i][j] == '2':
        dir = change_dir(dir)
        i = bi + i_[dir]
        j = bj + j_[dir]

        if i>= 0 and j>=0 and i<n and j<n and arr[i][j] == '1':
            now = (index, dir)
            return move(bi, bj, now, left)

        # 반대도 이동할 수 없다
        if i < 0 or j < 0 or i >= n or j >= n or arr[i][j] == '2':
            i = bi
            j = bj

        map[i][j].append((index, dir))
        horse[index] = (i,j)

        for r in range(len(left)):
            map[i][j].append(left[r])
            horse[left[r][0]] = (i,j)



    elif arr[i][j] == '0':
        map[i][j].append(now)
        horse[index] = (i,j)
        for r in range(len(left)):
            map[i][j].append(left[r])
            horse[left[r][0]] = (i,j)
    ## red
    else:

        for r in range(len(left)-1,-1,-1):
            horse[left[r][0]] = (i,j)
            map[i][j].append(left[r])

        map[i][j].append(now)

        horse[index] = (i,j)
        ## left가 존재할 경우는 따로 처리

    if len(map[i][j]) >= 4:
        return True




# 말이 한 턴씩 이동

def play():
    global k
    cnt = 0
    while cnt <= 1000:
        cnt += 1
        # print("round",cnt)
        # print('horse',horse)
        for i in range(1,k+1):
            r,c = horse[i]
            # print('to move',i)
            # pri(map)
            # # 같이 이동할 말x, 마지막에 홀로 존재
            # print(map[r][c])
            kan = map[r][c]


            if kan[len(kan)-1][0] == i:

                # 이미 지
                now = map[r][c].pop()
                re = move(r,c,now,[])

            # 같이 이동할 말 존재 ->
            # 말 이후의 것들은 같이 이동(list로 통째로 데려가고, 이후에 horse 배열 update)
            else:
                index = 0
                for t in range(len(kan)):
                    if kan[t][0] == i:
                        index = t
                        break

                now = kan[index]

                left = kan[index+1:]
                del map[r][c][index:]
                re = move(r,c,now,left)


            if re == True:
                return cnt

    return 1000

answer = play()

if answer == 1000 :
    print(-1)

else:
    print(answer)
# f.close()
