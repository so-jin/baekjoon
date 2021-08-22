# f = open("babyshark.txt", 'r')

# n원판 수 m 숫자 수 t 회전 횟수
# n, m, t = f.readline().split()
n,m,t = input().split()
n = int(n)
m = int(m)
t = int(t)
arr = [[0 for _ in range(m)] for _ in range(n+1)]
# 원판 숫자
for i in range(n):
    # line = f.readline().split()
    line = input().split()
    line = list(map(int, line))
    arr[i+1] = line
# start의 index
start = [0 for i in range(n+1)]

def pri(arr):
    for i in range(1,len(arr)):
        print(arr[i])

# x 원판 번호 d 방향 0시계/ 1반시계 k 칸 수
for r in range(t):
    # x, d, k = f.readline().split()
    x,d,k=input().split()
    x = int(x)
    d = int(d)
    k = int(k)
    if d == 0:
        k = m - k

    # 원판 복사
    narr = [[0 for _ in range(m)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m):
            narr[i][j] = arr[i][j]

    flag = 0
    # 배수의 원판 회전
    for w in range(x,n+1,x):
        start[w] = (start[w] + k) %m

    # 돌린 원판에 대해 같은 것 탐색
    for i in range(1,n):
        a = start[i]
        b = start[i+1]

        for q in range(m):
            if arr[i][a] and arr[i][a] == arr[i+1][b]:
                narr[i][a] = 0
                narr[i+1][b] = 0
                flag = 1
            a = (a + 1) % m
            b = (b + 1) % m

    # 원판 내에서 같은 숫자 제거
    for i in range(n+1):
        for j in range(m-1):
            if arr[i][j] and arr[i][j] == arr[i][j+1]:
                narr[i][j] = 0
                narr[i][j+1] = 0
                flag = 1
        if arr[i][0] and arr[i][0] == arr[i][m-1]:
            narr[i][0] = 0
            narr[i][m-1] = 0
            flag = 1

    if flag == 0:
        sum = 0
        cnt = 0
        for i in range(n+1):
            for j in range(m):
                if narr[i][j]:
                    sum += narr[i][j]
                    cnt += 1

        avg = sum / cnt
        for i in range(n+1):
            for j in range(m):
                if narr[i][j] and narr[i][j] < avg:
                    narr[i][j] += 1
                elif narr[i][j] and narr[i][j] > avg:
                    narr[i][j] -= 1
    arr = narr

sum = 0
for i in range(n+1):
    for j in range(m):
        sum+=arr[i][j]
print(sum)
# f.close()
