from itertools import combinations
from collections import deque

# f = open("in.txt","r")
# n = int(f.readline())
n = int(input())
# people = list(map(int, f.readline().split()))
people = list(map(int, input().split()))
m = [ [] for _ in range(n+1)]

sum = 0
for i in range(n) :
    sum += people[i]

for i in range(n):
    # 인접 지역 수,
    # m[i+1] = list(map(int, f.readline().split()))[1:]
    m[i+1] = list(map(int, input().split()))[1:]
graph = [x+1 for x in range(n)]

# 같은 선거구가 될 수 있는 지 확인하기
def check(group):
    global n
    V = [0 for _ in range(n+1)]
    cnt = 0
    que = deque()
    que.append(group[0])

    V[group[0]] = 1

    while que:
        now = que.pop()
        cnt += 1
        if cnt == len(group):
            return True
#         linked list로 주변 확인
        for next  in m[now] :
            if ( next in group ) and (V[next] == 0):
                que.append(next)
                V[next] = 1
    return False


result = 1000

for k in range(1,n//2+1):
    lst  = list(combinations(graph,k))


    for group in lst:

        # A group 에 대해서 한 선거구가 될 수 있는지 확인
        A = check(group)

        # B group
        not_group = []
        for i in range(1,n+1):
            if i not in group:
                not_group.append(i)

        # B group에 대해서 한 선거구가 될 수 있는지 확인
        B = check(not_group)

        # 둘 다 선거구가 될 수 있다면
        if A == True and B == True:
            A_sum = 0
            for i in group:
                A_sum += people[i-1]

            diff = sum- A_sum
            # 두 선거구의 인원 수 차이의 최솟값을 result에 저장
            result = min(abs(diff-A_sum),result)

if result == 1000:
    print(-1)
else:
    print(result)

