R, C, N = map(int, input().split())

map = [[-1] * C for _ in range(R)]
graph = []
for i in range(R):
    arr = list(input())
    graph.append(arr)
    for j in range(C):
        if arr[j] == 'O':
            map[i][j] = 0

def explode(array, bomb):
    r = len(array)
    c = len(array[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for x, y in bomb:
        array[x][y] = -1 #비워짐
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < r and 0 <= ny < c:
                    array[nx][ny] = -1 #비워짐

for t in range(1,N+1):
    bomb = set()
    if t == 1:
        for i in range(R):
            for j in range(C):
                if map[i][j] == -1:
                    continue
                map[i][j] += 1
    else:
        for i in range(R):
                for j in range(C):
                    map[i][j] += 1
                    if map[i][j] == 3:
                        bomb.add((i,j))
        
        if len(bomb) > 0:
            explode(map, bomb)

for xx in range(R):
        for yy in range(C):
            if map[xx][yy] < 0:
                print('.', end="")
            else:
                print('O', end="")
        print()

# 3 4 5
# O...
# ..O.
# O...