# f = open("in.txt","r")

count = int(input())
# count = int(f.readline())
score = 0
def pri(arr):
    for i in range(len(arr)-1,-1,-1):
        print(arr[i])


def find_place(arr, y):
    x = 4
    while x>=0:
        if arr[x][y] == 1:
            return x+1
        x -= 1
    return 0

def check_row(arr, i):
    for j in range(4):
        if arr[i][j] == 0:
            return 0
    return 1

def is_block(arr,i):
    for j in range(4):
        if arr[i][j] == 1:
            return 1
    return 0

def delete_row(arr):
    global score
    i = 0
    for cnt in range(4):
        if check_row(arr,i) == 1:
            score+=1
            del arr[i]
            arr.append([0 for _ in range(4)])
        else:
            i+=1


red = [[0 for _ in range(4)] for _ in range(4)]
blue = [[0 for _ in range(4)] for _ in range(6)]
green = [[0 for _ in range(4)] for _ in range(6)]

for k in range(count):
    # t,x,y = map(int, f.readline().split())
    t,x,y = map(int, input().split())
    #
    if t == 1:
        # 녹색
        put_x = find_place(green, y)
        green[put_x][y] = 1
#         blue
        put_x = find_place(blue, x)
        blue[put_x][x] = 1

    elif t == 2:
        put_x1 = find_place(green,y)
        put_x2 = find_place(green, y+1)
        put_x = max(put_x1, put_x2)
        green[put_x][y] = 1
        green[put_x][y+1] =1

#         blue
        put_x = find_place(blue, x)
        blue[put_x][x] = 1
        blue[put_x+1][x] = 1

    else:
        put_x = find_place(green,y)
        green[put_x][y] = 1
        green[put_x+1][y] = 1

        put_x1 = find_place(blue, x)
        put_x2 = find_place(blue, x+1)
        put_x = max(put_x1,put_x2)
        blue[put_x][x] = 1
        blue[put_x][x+1] = 1


#     배열 검사해서 가득찼으면 점수 더하기
# #
#     print("blue")
#     pri(blue)
#     print("----")
#     pri(green)
    delete_row(blue)
    delete_row(green)

    # 연한 부분
    i = 4
    for cnt in range(2):
        if is_block(green, i) == 1:
            del green[0]
            green.append([0 for _ in range(4)])
        else:
            i+=1
    i=4
    for cnt in range(2):
        if is_block(blue, i) == 1:
            del blue[0]
            blue.append([0 for _ in range(4)])
        else:
            i+=1
    # print("after del")
    # print("blue")
    # pri(blue)
    # print("----")
    # pri(green)
# 블록 갯수 계산
blocks = [blue, green]
block_cnt = 0
for b in blocks:
    for i in range(6):
        for j in range(4):
            if b[i][j] == 1:
                block_cnt+=1

print(score)
print(block_cnt)
