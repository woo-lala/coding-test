#17144
from collections import deque

R, C, T = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

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


def spread(queue):
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
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    
    up_x, up_y = air[0]
    
    dir = 0
    x, y = up_x, 1
    temp = map[x][y]
    map[x][y] = 0
    
    while True:
        
        x = x + dx[dir]
        y = y + dy[dir]
        
        if x == up_x and y == 0:
            break
        
        if 0 > x or x >= R or 0 > y or y >= C:
            x = x - dx[dir] #원상복귀
            y = y - dy[dir]
            
            dir = (dir + 1) % 4
            continue
        
        map[x][y], temp = temp, map[x][y]
    
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    down_x, down_y = air[1]
    
    dir = 0
    x, y = down_x, 1
    temp = map[x][y]
    map[x][y] = 0
    
    while True:
        
        x = x + dx[dir]
        y = y + dy[dir]
        
        if x == down_x and y == 0:
            break
        
        if 0 > x or x >= R or 0 > y or y >= C:
            x = x - dx[dir] #원상복귀
            y = y - dy[dir]
            
            dir = (dir + 1) % 4
            continue
        
        map[x][y], temp = temp, map[x][y]
    
    return map

for _ in range(T):
    q = find_dust(graph)
    temp_answer = spread(q)
    graph = rotate(temp_answer)

answer = 0
for i in range(R):
    answer += sum(graph[i])
    

print(answer + 2)