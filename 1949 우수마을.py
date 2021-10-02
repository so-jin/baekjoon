# recursion limit을 바꿔줘야 한다. 문제 상 마을의 최대 갯수 10^4
import sys
sys.setrecursionlimit(10**5)

size = int(input())
arr = list(map(int, input().split()))
link = [[] for _ in range(size)]
B = [0 for _ in range(size)]
V = [0 for _ in range(size)]

for i in range(size-1):
    a,b = map(int, input().split())
    link[a-1].append(b)
    link[b-1].append(a)

dp = [[0,0] for _ in range(size)]

# dp로 풀기!!
# dp[i][0] 포함 x
# dp[i][1] 포함 o
def cal(now):

    # visit을 언제 해야하는가?
    for i in link[now]:
        i -= 1
        if V[i] == 1:
            continue
        V[i] = 1
        # 자식에 대해 dp 계산
        cal(i)
        # now가 best면 자식 마을은 best가 아니어야 함
        dp[now][1] += dp[i][0]
        # now가 best가 아니면 자식 마을은 best일 경우, 아닐 경우 중 max를 가져옴
        dp[now][0] += max(dp[i][1], dp[i][0])

    # 현재 마을의 인구 수 추가
    dp[now][1] += arr[now]

V[0] = 1
cal(0)
print(max(dp[0][0], dp[0][1]))
