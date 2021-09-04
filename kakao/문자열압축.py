def solution(s):
    answer = len(s)

    if len(s) == 1:
        return 1
    for k in range(1,len(s)//2+1):
        # 시작점
        i = 0
        slen = 0
    # k는 문자열의 길이
        while True:
            ## 다를 때까지 비교해서 다르면 멈춘다. 길이 넘어가면 멈춘다.  
            
            # 남은 길이가 짧을 때, 버린다. 
            if i+2*k > len(s):
                slen += (len(s)-i)
                break
                
            same = 0
            while i+2*k <= len(s) and s[i:i+k] == s[i+k:i+2*k] :
                same += 1
                i += k 
                
            # 같은게 존재했다면
            if same > 0:
                same+=1
                while same//10 >0:
                    slen+=1
                    same = same//10
                slen += (k+1)
            # 모두 달랐다면
            else :
                slen += k
            i += k
            
            # if i+=k > len(s):
                # slen += (len(s)-i)
        answer = min(answer, slen)
    return answer
