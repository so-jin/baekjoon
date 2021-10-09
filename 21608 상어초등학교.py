# f = open("input.txt","r")

# n = int(f.readline())
n = int(input())
prefer = [[] for _ in range(n*n+1)]
order = []
arr = [[0 for _ in range(n)] for _ in range(n)]

for k in range(1, n*n+1):

    # input = list(map(int,f.readline().split()))
    inpu = list(map(int, input().split()))
    order.append(inpu[0])
    prefer[inpu[0]] = inpu[1:]

dx = [0,0,1,-1]
dy = [1,-1,0,0]


# 주변에 좋아하는 칸의 갯수와 비어 있는 칸의 갯수를 세기
def count(i,j, num):
    prefer_cnt = 0
    empty_cnt = 0
    for k in range(4):
        x = i+dx[k]
        y = j+dy[k]

        if x<0 or y<0 or x>=n or y>=n :
            continue
        if arr[x][y] == 0:
            empty_cnt+=1

        elif arr[x][y] in prefer[num]:
            prefer_cnt+=1

    return prefer_cnt, empty_cnt



# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.


arr[1][1] = order[0]

for k in order[1:]:
    max_prefer = -1
    max_empty = -1
    index = (0,0)

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                continue
            result = count(i,j, k)
            now_prefer = result[0]
            now_empty = result[1]

            if max_prefer == -1:
                max_prefer = now_prefer
                max_empty = now_empty
                index = (i,j)

            elif now_prefer > max_prefer:
                max_prefer = now_prefer
                max_empty = now_empty
                index = (i,j)

            elif now_prefer == max_prefer and now_empty > max_empty:
                max_empty = now_empty
                index = (i,j)

    arr[index[0]][index[1]] = k
    # print(arr)

answer = [0 for _ in range(5)]

# print(arr)
for i in range(n):
    for j in range(n):
        result = count(i,j,arr[i][j])
        answer[result[0]] +=1

# print(answer)

result = answer[1]*1 + answer[2]*10 + answer[3]*100 + answer[4]*1000
print(result)


