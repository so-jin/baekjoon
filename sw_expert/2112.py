import copy
# f = open("in.txt","r")
# test_num = int(f.readline())
test_num = int(input())
def pri(arr):
    for i in range(len(arr)):
        print(arr[i])
def check(arr, j, k):
    bef = -1
    cnt = 0
    for i in range(len(arr)):
        if bef == -1:
            bef = arr[i][j]
            cnt = 1
        elif bef == arr[i][j]:
            cnt+=1
        else:
            bef = arr[i][j]
            cnt = 1
        if cnt >= k:
            return True
    return False

def check_all(arr,k):
    for j in range(c):
        if check(arr,j,k) == False:
            return False
    return True

def change_row(arr, i, num):
    for j in range(len(arr[i])):
        arr[i][j] = num

def make_com(lst,k):
    ret = []
    if k>len(lst):
        return []
    if k == 1:
        for item in lst:
            ret.append([item])
    else:
        for i in range(len(lst)-k+1):
            for tmp in make_com(lst[i+1:], k-1):
                ret.append([lst[i]]+tmp)
    return ret


def find_min(arr,r):
    lst = [x for x in range(r)]

    for k in range(1, pass_num):
        coms = make_com(lst, k)
        # print(coms)
        for com in coms:
    #         A, B로 바꾸기
            tmp = copy.deepcopy(arr)
            for c in com:
                change_row(tmp,c,0)

                if check_all(tmp, pass_num):
                    # print('A')
                    # pri(tmp)
                    result = k
                    return result

            for c in com:
                change_row(tmp,c,1)
                if check_all(tmp, pass_num):
                    result = k
                    # print('B')
                    # pri(tmp)
                    return result
    return pass_num

for t in range(test_num):
    # r,c,pass_num = map(int, f.readline().split())
    r,c,pass_num = map(int, input().split())
    arr = []
    for i in range(r):
        # arr.append(list(map(int,f.readline().split())))
        arr.append(list(map(int,input().split())))
    if check_all(arr, pass_num):
        print("#"+str(t+1), 0)
        continue
    # print([x for x in range(r)])


    result = find_min(arr,r)

    print("#"+str(t+1),result)
