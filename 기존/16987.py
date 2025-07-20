#16987
import copy

N = int(input())
eggs_s = []
eggs_w = []

for _ in range(N):
    S, W = map(int, input().split())
    eggs_s.append(S)
    eggs_w.append(W)

M = -1e9
cnt = 0

def func(depth):
    global M, cnt
    
    if depth == N:
        M = max(M, cnt)
        return
    
    if eggs_s[depth] <= 0 or cnt == N-1:
        func(depth+1)
        return
    
    for i in range(N):
        if i == depth or eggs_s[i] <= 0:
            continue
        
        eggs_s[i] -= eggs_w[depth]
        eggs_s[depth] -= eggs_w[i]
        
        if eggs_s[i] <= 0:
            cnt += 1
        if eggs_s[depth] <= 0:
            cnt += 1
        func(depth+1)
        if eggs_s[i] <= 0:
            cnt -= 1
        if eggs_s[depth] <= 0:
            cnt -= 1
        
        eggs_s[i] += eggs_w[depth]
        eggs_s[depth] += eggs_w[i]
        

func(0)

print(M)