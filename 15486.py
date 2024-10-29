#15486
import sys
input = sys.stdin.readline

N = int(input())
plan = [[0, 0]]
dp = [0] * (N+1)

for i in range(N):
    plan.append(list(map(int, input().split())))
    

for i in range(1, N+1):
    dp[i] = max(dp[i-1],dp[i])
    
    index = i + plan[i][0] - 1
    
    if index <= N:
        temp = dp[i-1] + plan[i][1]
        dp[index] = max(dp[index], temp)

print(dp[N])
