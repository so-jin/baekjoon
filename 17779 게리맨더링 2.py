# f = open("in.txt","r")

# size = int(f.readline())
size= int(input())
arr = []
for i in range(size):
    # arr.append(list(map(int, f.readline().split())))
    arr.append(list(map(int, input().split())))


# 선거구 나누는건 대각선별로 진행
# 완전탐색
#
# 기준점 (x, y)와 경계의 길이 d1, d2를 정한다. (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
# 다음 칸은 경계선이다.
# (x, y), (x+1, y-1), ..., (x+d1, y-d1)
# (x, y), (x+1, y+1), ..., (x+d2, y+d2)
# (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
# (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)

# 전체 인구 수 구하기
total = 0
for i in range(size):
    for j in range(size):
        total += arr[i][j]

result = total
for x in range(0, size-2):
    for y in range(1, size-1):
        for d1 in range(1, size):
            for d2 in range(1, size):
                # x, y , d1, d2에 대해서 배열 크기 안에서 가능한 경우만
                if x+d1+d2 < size and y+d2 < size:

                    # 5번 구역 경계 표시
                    V = [[0 for _ in range(size)] for _ in range(size)]
                    # 각 구역별 인구 수
                    people = [0 for _ in range(5)]
                    # 5번 구역에 대해 경계 표시하기
                    for k in range(0, d1+1):
                        V[x+k][y-k] = 5
                    for k in range(0,d2+1):
                        V[x+k][y+k] = 5
                    for k in range(0,d2+1):
                        V[x+d1+k][y-d1+k] = 5
                    for k in range(0,d1 + 1):
                        V[x+d2+k][y+d2-k] = 5

                    # 1번 구역 인구 수
                    # row별로 탐색하면서 경계를 만나면 break
                    for i in range(x+d1):
                        for j in range(y+1):
                            if V[i][j] == 5:
                                break
                            people[0] += arr[i][j]

                    # 3번 구역 인구 수
                    for i in range(x+d1, size):
                        for j in range(y-d1+d2):
                            if V[i][j] == 5:
                                break
                            people[2] += arr[i][j]
                    #         2번 구역 인구 수
                    for i in range(x+d2+1):
                        for j in range(size-1, y, -1):
                            if V[i][j] == 5:
                                break
                            people[1] += arr[i][j]
                    #         4번 구역 인구 수
                    for i in range(x+d2+1, size):
                        for j in range(size-1, y+d2-d1-1,-1):
                            if V[i][j] == 5:
                                break
                            people[3] += arr[i][j]

                    # 5번 구역 인구 수
                    people[4] = total - people[0] - people[1] - people[2] - people[3]

                    people.sort()
                    # 인구 수 차이의 최댓값 구한뒤, 차이가 최소가 되는 경우를 저장
                    result = min(people[-1]  - people[0], result)


                # 1 35 / 2 36 / 3 18 / 4 35


print(result)
