#15486
import sys
input = sys.stdin.readline

N = int(input())
plan = []
memo = dict()
dp = [0] * (N+1)

for i in range(N):
    days, cost = map(int, input().split())
    
    index = days + i
    
    if index in memo:
        memo[index].append((i, cost))
    else:
        memo[index] = [(i, cost)]


for i in range(1,N+1):
    M = -1e9
    
    if i in memo:
        for d, c in memo[i]:
            temp = dp[d] + c
            if temp > M:
                M = temp
    dp[i] = max(dp[i-1], M)
            
print(dp[N])