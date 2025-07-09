from collections import deque

T = int(input())

def count_cabbage(arr, cabbage):
    q = deque()
    visited = set()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    cnt = 0
    x_len = len(arr)
    y_len = len(arr[0])
    
    for nx, ny in cabbage:
        if (nx, ny) not in visited:
            visited.add((nx, ny))
            q.append((nx, ny))
            while q:
                cur_x, cur_y = q.popleft()
                for d in range(4):
                    next_x = cur_x + dx[d]
                    next_y = cur_y + dy[d]
                    if 0 <= next_x < x_len and 0 <= next_y < y_len:
                        if arr[next_x][next_y] == 1 and (next_x, next_y) not in visited:
                            visited.add((next_x, next_y))
                            q.append((next_x, next_y))
            cnt += 1
    return cnt


for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    memo = set()
    for _ in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1
        memo.add((x,y))
    
    print(count_cabbage(graph, memo))