#programmers 문제

import copy

def solution(rows, columns, queries):
    arr = [[0] * columns for _ in range(rows)]
    num = 1
    result = []
    
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num
            num += 1
        
    def rotation(graph, x1, y1, x2, y2):
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        x, y = x1, y1
        temp = graph[x][y]
        d = 0
        m = 1e9
        
        while True:
            x = x + dx[d]
            y = y + dy[d]
            
            
            
            if x1 > x or x > x2 or y1 > y or y > y2:
                x = x - dx[d]
                y = y - dy[d]
                d = (d + 1) % 4
                continue
            
            graph[x][y], temp = temp, graph[x][y]    
            
            if graph[x][y] < m:
                m = graph[x][y]
            
            if x == x1 and y == y1:
                break
        
        return m
    
    answer = copy.deepcopy(arr)
    
    for a1, b1, a2, b2 in queries:
        result.append(rotation(answer, a1-1, b1-1, a2-1, b2-1))
                
    return result
