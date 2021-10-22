f =open("in.txt", "r")

# test_num = int(f.readline())
test_num = int(input())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
max_lenth = 0

def get_result(dp):
    result = 0
    for i in range(n):
        for j in range(n):
            result = max(result, max(dp[i][j][0], dp[i][j][1]))

    return result

# result  = 0
def dfs(i,j,flag,k,lenth):
    global result
    result = max(result, lenth)
    for d in range(4):
        x = i+dx[d]
        y = j+dy[d]

        if x<0 or y<0 or x>=n or y>=n or V[x][y] == 1:
            continue
        if arr[i][j] > arr[x][y]:
            V[x][y] = 1
            dfs(x,y,flag,k,lenth+1)
            V[x][y] = 0
        elif flag == 0 and arr[x][y] - arr[i][j] <k :
            tmp = arr[x][y]
            arr[x][y] = arr[i][j]- 1
            V[x][y] = 1
            dfs(x,y, 1, k,lenth+1)
            arr[x][y] = tmp
            V[x][y] = 0


def find_max():
    result = []
    high = 0
    for i in range(n):
        for j in range(n):
            high = max(high, arr[i][j])

    for i in range(n):
        for j in range(n):
            if arr[i][j] == high:
                result.append([i,j])

    return result
for t in range(test_num):
    n,k = map(int,input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    max_list = find_max()
    result = 0
    for start in max_list:
        V = [[0 for _ in range(n)] for _ in range(n)]
        V[start[0]][start[1]] = 1
        dfs(start[0],start[1],0,k,1)


    print("#"+str(t+1),result)

