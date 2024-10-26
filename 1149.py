#1149

N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))
dp = [(0,0,0)] * N

dp[0] = (cost[0][0], cost[0][1], cost[0][2])

for i in range(1, N):
    min_r = min(dp[i-1][1],dp[i-1][2]) + cost[i][0]
    min_g = min(dp[i-1][0],dp[i-1][2]) + cost[i][1]
    min_b = min(dp[i-1][0],dp[i-1][1]) + cost[i][2]
    
    dp[i] = (min_r, min_g, min_b)

print(min(dp[N-1]))