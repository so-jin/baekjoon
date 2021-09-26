from bisect import bisect_left, bisect_right
# f = open("in.txt","r")

# size = int(f.readline())
size = int(input())
# arr = list(map(int, (f.readline()).split()))
arr = list(map(int,input().split()))
lcs = []

for i in range(size):

    # 비어있으면 넣기
    if len(lcs) == 0 :
        lcs.append(arr[i])
    # 마지막 요소보다 크면 추가
    elif arr[i] > lcs[-1] :
        lcs.append(arr[i])
    #  right의 위치를 찾아서, right을 arr[i]로 바꾸기
    else:
#         맞는 위치 찾아가기
#         left = bisect_left(lcs,arr[i],0,len(lcs))
        right = bisect_right(lcs, arr[i], 0, len(lcs))
        lcs[right] = arr[i]

print(len(lcs))
