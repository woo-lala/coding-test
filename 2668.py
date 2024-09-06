# 숫자고르기

N = int(input())
graph = {}
for i in range(N):
    if i+1 not in graph:
        graph[i+1] = int(input())

answer = set()

def dfs(start, cur, visited):
    global answer
    
    if graph[cur] in visited:
        if start == cur:
            for x in visited:
                if x not in answer:
                    answer.add(x)
        return
    
    dfs(start, graph[cur], visited + [graph[cur]])

for i in range(1,N+1):
    dfs(i, i, [])
    
answer = list(answer)
answer.sort()

print(len(answer))
for v in answer:
    print(v)
    

# input
# 6
# 2
# 3
# 1
# 5
# 6
# 4
# output
# 6
# 1
# 2
# 3
# 4
# 5
# 6