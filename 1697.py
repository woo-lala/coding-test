from collections import deque

N, K = map(int, input().split())

visited = set()
q = deque()
q.append((N, 0))
dx = [-1, 1, 2]

while q:
    cur, distance = q.popleft()
    
    if cur == K:
        print(distance)
        break

    for d in range(3):
        if d == 2:
            next = cur * dx[d]
        else:
            next = cur + dx[d]
        
        if 0 <= next <= 100000:
            if next not in visited:
                q.append((next, distance + 1))
    
    
