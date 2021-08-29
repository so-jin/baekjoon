def tosec(time):
    time = time.split(':')
    
    return int(time[0])*3600 + int(time[1])*60 + int(time[2])

def tostr(time):
    if time < 10 :
        return '0'+str(time)
    return str(time)

def solution(play_time, adv_time, logs):
    answer = ''
    
    
    total = [0 for _ in range(360000)]
    for i in logs:
        i = i.split('-')
        start = tosec(i[0])
        
        end = tosec(i[1])
        total[start] += 1
        total[end] -= 1
        

    # 추가한 것에 대한 기록
    for i in range(1,360000):
        total[i] += total[i-1]
    
    # print(total[1500:3000])
    
    
    # 광고시간은 adv_time
    accum = [0 for _ in range(360000)]
    
    adv = tosec(adv_time)
    result = 0
    
    # 처음에 놓았을 때의 시간
    for i in range(adv):
        result += total[i]
    
    accum[0] = result 
    
    max_accum = result
    index = 0
    for i in range(1, 360000-adv+1):
        result += total[i+adv-1]
        result -= total[i-1]
        accum[i] = result
        if max_accum < result :
            max_accum = result
            index = i
        
    
    sec = index%60
    index = index //  60
    minute = index%60
    hour = index // 60
    
    

    answer = tostr(hour) + ':' +tostr(minute) + ':' + tostr(sec)
    

    return answer
