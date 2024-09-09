from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            baby_x, baby_y = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



fish_cnt = 0
baby_size = 2
answer = 0

while True:
#아래가 계속 반복된다
    visited = set() #need -> should be updated every time
    
    q = deque()
    q.append((baby_x, baby_y, 0))
    visited.add((baby_x, baby_y))

    possible_fish = []
    min_distance = 1e9


    while q:
        cur_x, cur_y, cur_cnt = q.popleft()
        
        if graph[cur_x][cur_y] < baby_size and graph[cur_x][cur_y] != 0:
            if min_distance >= cur_cnt:
                min_distance = cur_cnt
                possible_fish.append((cur_x, cur_y)) 
                
        for d in range(4):
            next_x = cur_x + dx[d]
            next_y = cur_y + dy[d]
        
            if 0 <= next_x < N and 0 <= next_y < N:
                if (next_x, next_y) not in visited:
                    q.append((next_x, next_y, cur_cnt+1))
                    visited.add((next_x, next_y))
                    
    possible_fish.sort(key=lambda x : (x[0], x[1]))
    

    if possible_fish:
        graph[baby_x][baby_y] = 0
        baby_x, baby_y = possible_fish[0]
        graph[baby_x][baby_y] = 9
        answer += min_distance
        fish_cnt += 1
        if fish_cnt == baby_size:
            fish_cnt = 0
            baby_size += 1
    else:    
        break
    
    print(possible_fish, answer, min_distance)
    for g in graph:
        print(g)

print(answer)