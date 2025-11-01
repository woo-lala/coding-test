N = int(input())
small = []
big = []
for _ in range(N-1):
    small_jump, big_jump = map(int, input().split())
    
    small.append(small_jump)
    big.append(big_jump)
K = int(input())

INF = 10**9
dp = [[INF] * 2 for _ in range(N)]

dp[0][0] = 0

if N >= 2:    
    dp[1][0] = small[0]
if N >= 3:    
    dp[2][0] = min(dp[1][0] + small[1], big[0])

for i in range(3, N):
    dp[i][0] = min(dp[i-1][0] + small[i-1], dp[i-2][0] + big[i-2])
    dp[i][1] = min(dp[i-1][1] + small[i-1], dp[i-2][1] + big[i-2], dp[i-3][0] + K)

print(min(dp[N-1][0], dp[N-1][1]))