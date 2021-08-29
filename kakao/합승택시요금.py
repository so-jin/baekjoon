from queue import PriorityQueue

graph = {}

def get_minfare(d, s):
    que = PriorityQueue()
    que.put((0,s))
    num = 5
    d[s] = 0
    while que.empty() == False:
        # num -=1
        now = que.get()
        dist = now[0]
        ver = now[1]
        
        if d[ver] == dist and ver in graph:
            nlist = graph[ver]
            
    
            for nex in nlist:
                # 방문한 적이 없으면
            
                nver = nex[0]
                ndist = nex[1]
                if d[nver] == -1 or d[nver] > dist + ndist:
                    d[nver] = dist + ndist
                    que.put((d[nver],nver))
            # break

def solution(n, s, a, b, fares):
    # n 지점 개수 s출발 a도착 b도착 fares 택시 요금
    # 각 지점별로 동시에 갔을 때, 
    # a, b, s에서 각 지점까지의 최단거리를 구해야 함
    # 다 구한 뒤 계산
    answer = 0
    
    ds = [-1 for _ in range(n+1)]
    da = [-1 for _ in range(n+1)]
    db = [-1 for _ in range(n+1)]
    
    # linked list 형태로 연결 지점 기록
    
    for i in fares:
        if i[0] in graph:
            graph[i[0]].append((i[1],i[2]))
        else :
            graph[i[0]] = [(i[1],i[2])]
        if i[1] in graph:
            graph[i[1]].append((i[0],i[2]))
        else:
            graph[i[1]] = [(i[0],i[2])]
    
    get_minfare(ds, s)
    get_minfare(da, a)
    get_minfare(db,b)
    
    
    #거리 계산하기 
    result = 20000000
    for i in range(1, n+1):
        if ds[i] != -1 and da[i] != -1 and db[i] != -1:
            dist = ds[i] + da[i] + db[i]
            if result > dist :
                result = dist
    
    answer = result
    return answer
