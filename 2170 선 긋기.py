# list에서 tuple로 바꾸니 문제가 풀림
# f = open("in.txt","r")

# num = int(f.readline())
num = int(input())
arr = []
for i in range(num):
    # arr.append(list(map(int, f.readline().split())))
    a,b = map(int, input().split())
    arr.append((a,b))

arr.sort()

# 초기 좌측, 우측 값 
l = float("inf")
r = float("-inf")


sum = 0
for str in arr:
    # 우측 값보다 현재 좌측 값이 더 크면, string이 분리되는 것 
    if str[0] > r:
        # 새로운 string에 대해 탐색하므로 이전 string 길이 저장 
        if r-l > 0:
            sum+= r-l

        l = str[0]
        r = str[1]
    # 시작점은 원래 string에 포함되나, 끝나는 지점이 다를 때, 길이 연장 
    elif str[1]>r:
        r = str[1]

sum += r-l

print(sum)
