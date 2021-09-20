# f = open("in.txt")

# num = int(f.readline())
arr = []
num = int(input())
for i in range(num):
    # line = (f.readline()).split()
    line = input().split()
    arr.append(list(map(int,line)))

end = 1
end <<= num
dp = [ [ 0 for _ in range(end)] for _ in range(num)]
end-=1

def travel(now, flag):
    global min_dist
    global num
    # 다 방문했을 때,
    if flag == end:
        if arr[now][0] > 0 :
            return arr[now][0]
    # 이미 방문했을 
    if dp[now][flag] != 0:
        return dp[now][flag]
    dp[now][flag] = 20000000

    for i in range(num):
        # 길이 없다
        if arr[now][i] == 0 :
            continue
        # 이미 route에 존
        if (flag&(1<<i)) == (1<<i) :
            continue

        dp[now][flag] = min( dp[now][flag], arr[now][i] +travel(i, flag | 1<<(i)) )
    return dp[now][flag]

print(travel(0,1))

