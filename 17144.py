#17144
from collections import deque

R, C, T = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(map(int, input().split())))

air = []

for i in range(R):
    if graph[i][0] == -1:
        air.append((i, 0))
        air.append((i+1, 0))
        break          

def find_dust(graph):
    q = deque()
    for i in range(R):
        for j in range(C):
            if graph[i][j] != -1 and graph[i][j] != 0:
                q.append((i, j))
    return q


def bfs(queue):
    global graph
    temp_graph = [[0]* C for _ in range(R)]
    for x, y in air:
        temp_graph[x][y] = -1
        
    while queue:
        cur_x, cur_y = queue.popleft()
        cnt = 0
        
        spread = graph[cur_x][cur_y] // 5
        for d in range(4):
            next_x = cur_x + dx[d]
            next_y = cur_y + dy[d]
            
            if 0 <= next_x < R and 0 <= next_y < C:
                if (next_x, next_y) not in air:
                    cnt += 1
                    temp_graph[next_x][next_y] += spread
        
        temp_graph[cur_x][cur_y] = temp_graph[cur_x][cur_y] + graph[cur_x][cur_y] - (cnt * spread)

    return temp_graph

def rotate(map):
    up_x, up_y = air[0]
    
    for i in range(up_x, -1, -1):
        cur_x, cur_y = i, 0
        next_x, next_y = i-1, 0
        
        if 0 > next_x or next_x >= R:
            break
        
        if map[cur_x][cur_y] == -1:
            continue
        
        map[cur_x][cur_y] = map[next_x][next_y]

    for i in range(C):
        cur_x, cur_y = 0, i
        next_x, next_y = 0, i+1
        
        if 0 > next_y or next_y >= C:
            break
        
        if map[cur_x][cur_y] == -1:
            continue
        
        map[cur_x][cur_y] = map[next_x][next_y]
    
    for i in range(0, up_x+1):
        cur_x, cur_y = i, C-1
        next_x, next_y = i+1, C-1
        
        if 0 > next_x or next_x >= R:
            break
        
        if map[cur_x][cur_y] == -1:
            continue
        
        map[cur_x][cur_y] = map[next_x][next_y]
    
    for i in range(C-1, -1, -1):
        cur_x, cur_y = up_x, i
        next_x, next_y = up_x, i-1
        
        if 0 > next_y or next_y >= C:
            break
        
        if map[next_x][next_y] == -1:
            map[cur_x][cur_y] = 0
            continue
        
        map[cur_x][cur_y] = map[next_x][next_y]
    
    
    down_x, down_y = air[1]
    
    for i in range(down_x, R):
        cur_x, cur_y = i, 0
        next_x, next_y = i+1, 0
        
        if 0 > next_x or next_x >= R:
            break
        
        if map[cur_x][cur_y] == -1:
            continue
        
        map[cur_x][cur_y] = map[next_x][next_y]

    for i in range(C):
        cur_x, cur_y = R-1, i
        next_x, next_y = R-1, i+1
        
        if 0 > next_y or next_y >= C:
            break
        
        if map[cur_x][cur_y] == -1:
            continue
        
        map[cur_x][cur_y] = map[next_x][next_y]
    
    
    for i in range(R-1, down_x-1, -1):
        cur_x, cur_y = i, C-1
        next_x, next_y = i-1, C-1
        
        if 0 > next_x or next_x < down_x:
            break
        
        if map[cur_x][cur_y] == -1:
            continue
        
        map[cur_x][cur_y] = map[next_x][next_y]
    
    for i in range(C-1, -1, -1):
        cur_x, cur_y = down_x, i
        next_x, next_y = down_x, i-1
        
        if 0 > next_y or next_y >= C:
            break
        
        if map[next_x][next_y] == -1:
            map[cur_x][cur_y] = 0
            continue
        
        map[cur_x][cur_y] = map[next_x][next_y]
    
    return map


for _ in range(T):
    q = find_dust(graph)
    temp_answer = bfs(q)
    graph = rotate(temp_answer)



answer = 0
for i in range(R):
    answer += sum(graph[i])
    

print(answer + 2)