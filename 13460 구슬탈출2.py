
m, n = input().split()
m = int(m)
n = int(n)

arr = []
for i in range(int(m)):
    # line = f.readline()
    line = input()
    arr.append(list(line)[0:n])

ri = 0
rj = 0
bi = 0
bj = 0
answer = 11

V =[[[ [0 for _ in range(n)] for _ in range(m)] for _ in range(n) ] for _ in range(m)]

# V_b =[ [0 for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        if arr[i][j] == 'R':
            ri = i
            rj = j
        if arr[i][j] == 'B':
            bi = i
            bj = j


V[ri][rj][bi][bj] = 1
i_ = [0,0,-1,1]
j_ = [1,-1,0,0]

def move( i, j , i_dir, j_dir):
    while arr[i+i_dir][j+j_dir] != '#':
        i += i_dir
        j += j_dir
        if arr[i][j] == 'O':
            # print('find O')
            return i, j
    return i, j

def pri():
    for i in range(len(arr)):
        print(arr[i])

def dfs(ri,rj,bi,bj,cnt):
    global answer
    # print('cnt', cnt,ri,rj,bi,bj)
    # pri()
    if cnt == 10 :
        return
    for k in range(4):
        nr = move(ri , rj, i_[k], j_[k])
        nb = move(bi, bj, i_[k], j_[k])
        # print(nr, nr[0], nb)
        if arr[nb[0]][nb[1]] == 'O':
            continue

        ## 구멍 발견
        if arr[nr[0]][nr[1]] == 'O':
            # print('answer',answer, cnt+1)
            answer = min(answer, cnt+1)
            return

        ## 같은 곳에 있으면 위치 이동 필요
        if nr == nb:
            # print('same direct',nr)
            ## r이 앞에 존
            if ri - bi == 0 and (rj - bj)*j_[k] >= 1:
                nb = (nb[0]-i_[k], nb[1]-j_[k])

            elif rj - bj ==0 and (ri - bi) *i_[k] >= 1:
                nb = (nb[0]-i_[k], nb[1]-j_[k])
            else:
                nr = (nr[0]-i_[k], nr[1]-j_[k])

            # print(nr,nb)



        if V[nr[0]][nr[1]][nb[0]][nb[1]] == 0:
            V[nr[0]][nr[1]][nb[0]][nb[1]] = 1
            arr[ri][rj] = '.'
            arr[bi][bj] = '.'

            arr[nr[0]][nr[1]] = 'R'
            arr[nb[0]][nb[1]] = 'B'
            # print(cnt, nr,nb)
            # pri()
            dfs(nr[0],nr[1],nb[0],nb[1], cnt+1)


            arr[nr[0]][nr[1]] = '.'
            arr[nb[0]][nb[1]] = '.'

            arr[ri][rj] = 'R'
            arr[bi][bj] = 'B'
            V[nr[0]][nr[1]][nb[0]][nb[1]] = 0




dfs(ri, rj,bi,bj, 0)
if answer == 11 :
    print(-1)
else :
    print(answer)

# f.close()
