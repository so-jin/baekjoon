# f = open("babyshark.txt", 'r')

# r, c, num = f.readline().split()
r, c, num = input().split()
# n,num, m = f.readline().split()
# m, n = input().split()
r = int(r)
c = int(c)
num = int(num)
arr = [ [[] for _ in range(c+1)] for _ in range(r+1)]
## r c speed direct size cnt

def pri():
    for i in range(1,r+1):
        print(arr[i][1:])

for i in range(int(num)):
    # m, n, s, d, size = f.readline().split()
    # line = input()
    m, n, s, d, size = input().split()
    # inp = list(line)[0:5]
    # arr.append(list(line)[0:n])
    # arr.append(list(map(str, line.split(""))))
    d = int(d)
    s = int(s)

    if d == 1 or d == 2 :
        arr[int(m)][int(n)].append((s, d, int(size), 1))
    else:
        arr[int(m)][int(n)].append((s,int(d),int(size),1))


# pri()
sum = 0


def go(i, j , s ,dir):
    global r,c
    # up
    if dir == 1:
        if i-s <=0:
            s = -(i-s)
            s += 1
            return go(1,j,s, 2)
        return i-s, j, 1
    # down
    elif dir == 2:
        if i+s>r:
            s = i+s-r
            return go(r,j,s,1)
        return i+s, j ,2
    # ->
    elif dir == 3:
        if j+s>c:
            s = j+s-c
            return go(i,c,s,4)
        return i,j+s,3
    # <-
    else:
        if j-s <= 0 :
            s = -(j-s)
            s += 1
            return go(i, 1,s,3)
        return i,j-s,4


def eat(re,shark):
    ne = arr[re[0]][re[1]]
    flag = 0

    for i in range(len(ne)):
        if ne[i][3] == shark[3]:
            flag = 1

    ## 이미 상어가 존재하면
    if flag:
        # 새 상어가 더 크면
        if ne[len(ne)-1][2] < shark[2]:
            ne[len(ne)-1] = shark
    else:
        arr[re[0]][re[1]].append(shark)


## 낚시왕 이동
for j in range(1, c+1):
    # 가까운 상어 낚시
    for i in range(1, r+1):
        # 상어가 존재할 때 한마리만 낚시

        if arr[i][j] :
            # print(arr[i][j])
            sum += arr[i][j][0][2]
            arr[i][j] = []
            break

    # 다른 상어들 이동
    for si in range(1, r+1):
        for sj in range(1, c+1):
            # 상어가 존재하면 칸 이동, 단 아직 이동하지 않은 상어만 이동
            if arr[si][sj] and arr[si][sj][0][3] == j:
                shark = arr[si][sj][0]
                # 상어 이동
                re = go(si,sj, shark[0],shark[1])

                del arr[si][sj][0]
                shark = (shark[0], re[2], shark[2], j+1)

                # 이동한 상어 여러마리면 먹
                eat(re,shark)

print(sum)
