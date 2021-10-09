# f = open("in.txt","r")

# n,m = map(int, f.readline().split())
n,m = map(int, input().split())
lst = []
arr = [0 for _ in range(n*n)]

num_index = [7,3,1,5]

num_dist = [15,11,9,13]
del_ball = [0,0,0,0]
# 간격은 8, 등비급수??

# 달팽이 방향
dx = [0,1,0,-1]
dy = [-1,0,1,0]

for i in range(n):
    # lst.append(list(map(int,f.readline().split())))
    lst.append(list(map(int, input().split())))

magic = []
for i in range(m):
    # magic.append(list(map(int, f.readline().split())))
    magic.append(list(map(int, input().split())))

# graph를 1차원으로 변경
def re_arrange():
    i = n//2
    j = n//2
    k = 0
    flag = 0
    dir = -1
    len = 0
    while k < n*n:
        dir = (dir+1)%4
        if flag == 0:
            flag = 1
            len += 1
        else:
            flag = 0

        for t in range(len):
            if k!= 0 and lst[i][j] == 0:
                return
            arr[k] = lst[i][j]
            k += 1
            i += dx[dir]
            j += dy[dir]
# 구슬 폭파
def delete(k):
    dir = magic[k][0] - 1
    dist = magic[k][1]

    index = num_index[dir]
    diff = num_dist[dir]
    for i in range( dist):
        if index >= len(arr):
            return
        del arr[index]
        index += diff-1
        diff += 8

# 같은 구슬끼리 제거하고, 0 인 것도 제거
def del_group():
    global arr
    new_arr = [0]
    i = 1
    result = 0
    # 길이가 2.3같이 작을 때 대처!!
    if len(arr) == 2:
        return 0


    while i< len(arr)-1:
        # if arr[i] == 0:
        #     i+=1
        #     continue
        if arr[i] != arr[i+1]:
            new_arr.append(arr[i])
        else:
            cnt = 0
            while i<len(arr)-1 and arr[i] == arr[i+1]:
                cnt+= 1
                i+=1

            if cnt<3:
                for k in range(cnt+1):
                    new_arr.append(arr[i])
            else:
                result += 1
                del_ball[arr[i]] += cnt+1

        i+=1

    if i < len(arr) and arr[i]!= 0 :
        new_arr.append(arr[i])
    # 마지막 배열 원소 추가


    arr = new_arr
    return result

# 구슬을 갯수와 구슬 번호로 분리
def seperate_ball():
    global arr
    new_arr = [0]
    i=1
    while i< len(arr)-1 and len(new_arr) < n*n:
        cnt = 0
        while i< len(arr)-1 and arr[i] == arr[i+1]:
            cnt+=1
            i+=1

        new_arr.append(cnt+1)
        if len(new_arr) < n*n:
            new_arr.append(arr[i])

        i+=1

    if i<len(arr) and len(new_arr) < n*n:
        new_arr.append(1)

        if len(new_arr) < n*n:
            new_arr.append(arr[i])
    arr = new_arr



re_arrange()

for i in range(m):

    delete(i)
    # 제거할 그룹이 없을 때까지 제거
    while del_group() :
        continue
    # 그룹의 구슬 세기
    seperate_ball()

print(del_ball[1] + del_ball[2]*2 + del_ball[3]*3)
