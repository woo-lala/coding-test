#14889

N = int(input())
arr = []
all = 0
team = [0] * (N//2)
for _ in range(N):
    a = list(map(int, input().split()))
    arr.append(a)

visited = [False] * N

M = 1e9

def count(t):
    result = 0
    for x in t:
        for j in range(N):
            if x == j:
                continue
            if j in t:
                result += arr[x][j]
    return result

def func(depth, st):
    global M
    if depth == N//2:
        
        team_sum = count(team)
        other_team = []
        for x in range(N):
            if x not in team:
                other_team.append(x)
        
        other_sum = count(other_team)
        
        if other_sum >= team_sum:
            difference = other_sum - team_sum
        else:
            difference = team_sum - other_sum
        
        if difference == 0:
            M = 0
        else:
            M = min(M, difference)

        return
    
    for i in range(st, N):
        if not visited[i]:
            visited[i] = True
            team[depth] = i
            func(depth+1, i+1)
            visited[i] = False

func(0, 1)

print(M)