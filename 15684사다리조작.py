from collections import deque

# f = open("babyshark.txt", 'r')

# n,num, m = f.readline().split()
n, num, m = input().split()
# size = int(input())
arr = []
for i in range(int(num)):
    # line = f.readline()
    line = input()
    arr.append( list(map(int, line.split())) )

m = int(m)
n = int(n)

ladd = [[0 for _ in range(n+1)] for _ in range(m+1) ]
graph = [[] for _ in range(n+1)]

for i in range(int(num)):
    ladd[arr[i][0]][arr[i][1]] = 1
    graph[arr[i][1]].append(arr[i][0])




answer = 999
def check(ladd):
    global m,n
    for start in range(1,n):
        # print('col', start)
        j = start
        for i in range(1,m+1):
            # print( i , j)
            if ladd[i][j] == 1:
                # print('right')
                j +=1
            elif ladd[i][j-1] == 1:
                # print('left')
                j -=1
        if j!= start :
            # print(i, j, start)
            return False
    return True

# print(check(ladd))


def place(ladd,  i_st, j_st, sum) :
    global answer
    if check(ladd) :
        # print( 'fin')
        answer = min(sum, answer)
        return
    if sum == 3 :
        # print(ladd)
        # print('over 3')
        return
    # print(sum, index, sum)
    # if index == n and check(ladd):
    #     return sum
    # if sum == 3 :
    #     for i in range (index, n):
    #         if col[i]%2 == 1 or check(ladd):
    #             print('over 3')
    #             return -1
    #         return sum
    for j in range(j_st, n):

        if ladd[i_st][j] == 1:
            continue
        if j - 1 < 0 or ladd[i_st][j - 1] == 1:
            continue
        if j + 1 > n or ladd[i_st][j + 1] == 1:
            continue
        ladd[i_st][j] = 1
        place(ladd, i_st, j + 1, sum + 1)
        ladd[i_st][j] = 0

    for i in range(i_st+1, m+1):
        ## do something
        #find something to add
        for j in range(1, n):

            if ladd[i][j] == 1 :
                continue
            if j-1<0 or ladd[i][j-1] == 1 :
                continue
            if j+1>n or ladd[i][j+1] == 1:
                continue
            ladd[i][j] = 1
            place(ladd, i, j+1, sum+1)
            ladd[i][j] = 0


     # return sum

# print(check(ladd))
place(ladd,  1,1, 0 )



if answer == 999:
    print(-1)
else:
    print(answer)









# f.close()

