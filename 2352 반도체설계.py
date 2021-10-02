from bisect import bisect_left, bisect_right

size = int(input())
# arr = list(map(int, (f.readline()).split()))
arr = list(map(int,input().split()))
lis = []

# lis를 기억하는 것이 아니라, lis의 길이만 알면 된다.
for i in range(size):
    # 비어있으면 넣기
    if len(lis) == 0 :
        lis.append(arr[i])
    # 마지막 요소보다 크면 추가
    elif arr[i] > lis[-1] :
        lis.append(arr[i])
    #  right의 위치를 찾아서, right을 arr[i]로 바꾸기
    else:
#         맞는 위치 찾아가기
#         left = bisect_left(lcs,arr[i],0,len(lcs))
        right = bisect_right(lis, arr[i], 0, len(lis))
        lis[right] = arr[i]

print(len(lis))
