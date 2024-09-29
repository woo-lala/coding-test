#15650

N, M = map(int, input().split())

arr = [i for i in range(1,N+1)]
new = [0] * M
visited = [False] * N

def func(depth, st):
    if depth == M:
        for i in new:
            print(i, end =" ")
        print()
        return
    
    for i in range(st, N):
        if not visited[i]:
            new[depth] = arr[i]
            visited[i] = True
            func(depth+1, i+1)
            visited[i] = False
        
func(0, 0)