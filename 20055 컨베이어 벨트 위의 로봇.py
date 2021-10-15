# deque를 이용해서 풀면 더 빠르게 풀 수 있을것, rotate는 deque를 사용해보자
n, k = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
end = n-1
empty_cnt = 0
robot_on = [0 for _ in range(2*n)]
robot_lst = []

time =0
while True:
    time+=1

    # 벨트 이동
    start = (start-1) % (2*n)
    end = (end-1) % (2*n)
    # end지점에 로봇이 있으면?
    if robot_on[end] != 0:
        robot_on[end] = 0

    # 로봇 이동 end 부터 start까지 돌면 된다.
    i = (end) % (2 * n)


    while True:
        i = (i-1)%(2*n)
        next = (i+1)%(2*n)
        if robot_on[i] >0 and robot_on[next] == 0 and arr[next] > 0:

            robot_on[next] = robot_on[i]
            robot_on[i] = 0
            arr[next] -= 1

        # 끝점에 도달
        if next == end:
            robot_on[end] = 0

        # 시작점에 도달
        if i == start:
            # 내구도가 남아있으면 올리기
            if arr[i] > 0:
                arr[i] -= 1
                robot_on[i] = 1
            break


    cnt = 0
    for i in range(2*n):
        if arr[i] <= 0:
            cnt+=1

    if cnt>=k:
        print(time)
        break



