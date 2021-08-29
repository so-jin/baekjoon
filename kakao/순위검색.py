from itertools import combinations        
from bisect import bisect_left


def make_pair(info):
    cases = []
    for k in range(5):
        li = list(combinations([0,1,2,3],k))  
        for l in li:
            case = ''
            for i in range(4):
                if i in l:
                    case+=info[i]    
                else:
                    case+='-'
            cases.append(case)
    return cases


def solution(info, query):
    answer = []
    folio = []
    dict = {}
    for i in info:
        inform = i.split()
        
        re = make_pair(inform)
        
        for j in re :
            if j in dict:
                dict[j].append(int(inform[4]))
                
            else:
                dict[j] = [int(inform[4])]
        
    for key in dict:
        dict[key].sort()
    
    for i in query:
        s = i.split()
        search = s[0] + s[2] + s[4] + s[6]
        # print(search)
        if search in dict:    
            num = int(s[7])
            # answer.append(len(dict[search]) - bisect_left(dict[search], num, lo=0, hi=len(dict[search])))
            start = 0
            end = len(dict[search])
            mid = (start+end)//2
            num = int(s[7])
            
            
            while start < end:
                if dict[search][mid] < num:
                    start = mid+1
                    mid = (start+end)//2
                else : 
                    end = mid
                    mid = (start+end)//2
            answer.append((len(dict[search])-start))
        else:
            answer.append(0)
    
    return answer
