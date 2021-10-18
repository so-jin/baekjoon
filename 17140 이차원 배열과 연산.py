# f = open("in.txt","r")


# r, c, k = map(int, f.readline().split())
r,c,k = map(int, input().split())
arr = []
for i in range(3):
    # arr.append(list(map(int, f.readline().split())))
    arr.append(list(map(int, input().split())))

def pri(arr):
    for i in range(len(arr)):
        print(arr[i])
def row_cal():
    global arr
    row_lst = []
    max_row = 0
    for i in range(len(arr)):
        lst = arr[i]

        dic = {}

        for j in range(len(lst)):
            if arr[i][j] == 0:
                continue
            elif arr[i][j] in dic:
                dic[arr[i][j]] += 1
            else:
                dic[arr[i][j]] = 1


        dic = sorted(dic.items(), key = lambda x:(x[1], x[0]))

        # print(dic)
        max_row = max(max_row, len(dic)*2)
        row_lst.append(dic)

    new_arr = [[0 for _ in range(min(100,max_row))] for _ in range(len(arr))]

    for i in range(len(arr)):
        lst = row_lst[i]

        for j in range(min(50,len(lst))):
            new_arr[i][j*2] = lst[j][0]
            new_arr[i][j*2+1] = lst[j][1]

    arr = new_arr
    # print("row")
    # pri(arr)
        # lst = []
        # for item in dic:
        #     # 100개가 넘어가면 버리기
        #     if len(lst) >= 100:
        #         break
        #     lst.append(item[0])
        #     lst.append(item[1])
        # arr[i] = lst


def col_cal():
    global arr
#     j의 크기를 구하기
    max_col = 0
    for i in range(len(arr)):
        max_col = max(max_col, len(arr[i]))

    col_lst = []
    max_row = 0
    for j in range(max_col):
        dic = {}
        for i in range(len(arr)):
            if j >= len(arr[i]) or arr[i][j] == 0:
                continue
            if arr[i][j] in dic:
                dic[arr[i][j]] += 1
            else:
                dic[arr[i][j]] = 1

        dic = sorted(dic.items(), key =  lambda x : (x[1], x[0]))
        col_lst.append(dic)
        max_row = max(max_row, len(dic)*2)

    # print("col")
    # print(col_lst)

    new_arr = [[0 for _ in range(max_col)] for _ in range(min(max_row, 100))]
    for j in range(max_col):
        lst = col_lst[j]
        for i in range(min(len(lst), 50) ):
            new_arr[i*2][j] = lst[i][0]
            new_arr[i*2+1][j] = lst[i][1]
    # pri(new_arr)
    arr = new_arr

time=0


while time<=100:
    if len(arr)>r-1 and len(arr[0]) > c-1 and arr[r-1][c-1] == k:
        print(time)
        break
    time+=1

    if len(arr) >= len(arr[0]):
       row_cal()
    else:
       col_cal()
# col_cal()
if time > 100:
    print(-1)
