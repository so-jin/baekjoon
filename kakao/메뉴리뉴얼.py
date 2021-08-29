from itertools import combinations 
import operator

def solution(orders, course):
    
    
    ## 음식별로 조합 만들기, 그리고 그 조합 세기
    answer = []
    for k in course:
        dic = {}
        for order in orders:
            
            com = list(combinations(order,k))
            for menu in com:
                men = list(menu)
                men = sorted(men)
                # print(men)
                men = ''.join(men)
                if men in dic:
                    dic[men] = dic[men] +1
                else :
                    dic[men] = 1
        sdict = sorted(dic.items(), key=operator.itemgetter(1),reverse = True)
        
        if sdict and sdict[0][1] >1 :
            maxval = sdict[0][1]
            
            for menu in sdict:
                if menu[1] == maxval:
                    answer.append(menu[0])
                    
                else:
                    break
    answer.sort()
    
    return answer
