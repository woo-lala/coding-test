from collections import deque
import sys

#입력
graph = []
m, n = map(int,input().split())
for i in range(n):
    graph.append(list(map(int, input().split())))  
q = deque()

cnt_1 = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt_1 += 1

if cnt_1 == (n * m):
    print(0)
    sys.exit(0)


#최소일수 구하기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j,0))
            

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    cur_x, cur_y, cur_day = q.popleft()
    for d in range(4):
        next_x = cur_x + dx[d]
        next_y = cur_y + dy[d]
        if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m:
            if graph[next_x][next_y] == 0:
                graph[next_x][next_y] = 1
                next_day = cur_day + 1
                q.append((next_x, next_y, next_day))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            sys.exit(0)

print(cur_day)