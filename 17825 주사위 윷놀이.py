# f = open("in.txt","r")

arr = [x for x in range(33)]

for x in range(21):
    arr[x] = x*2

arr[21] = 13
arr[22] = 16
arr[23] = 19
arr[24] = 22
arr[25] = 24
arr[26] = 28
arr[27] = 27
arr[28] = 26
arr[29] = 25
arr[30] = 30
arr[31] = 35
arr[32] = 0

next = [[x+1] for x in range(33)]
next[5] = [6,21]
next[10] = [11,24]
next[15] = [16,26]
next[23] = [29]
next[25] = [29]
next[31] = [20]
next[20] = [32]
next[32] = [32]

# dices = list(map(int, f.readline().split()))
dices = list(map(int, input().split()))
dice_num = [0 for x in range(5)]
for x in dices:
    dice_num[x-1] += 1

horses = [ 0 for _ in range(4)]
def move(x, move_cnt):
    # 말 위치 변경
    now = horses[x]
    if len(next[now]) >1 :
        now = next[now][1]
    else:
        now = next[now][0]

    for k in range(move_cnt-1):
        now = next[now][0]

    if now in horses and now!=32:
        return -1
    return now

max_score = 0
def dfs(index, score):
    global max_score
    if index == 10:
        max_score = max(max_score, score)
        return score

    for x in range(4):

        bef = horses[x]
        nex = move(x,dices[index])
        if horses[x] == 32:
            continue
        if nex != -1:
            horses[x] = nex
            dfs(index+1, score+arr[horses[x]])
            horses[x] = bef

dfs(0,0)
print(max_score)
