#10844

import copy

N = int(input())

dp = [0] * 10


for i in range(1, 10):
    dp[i] = 1


for i in range(N-1):
    tmp = [0] * 10    
    for i in range(10):
        if 0<= i-1 <= 9:
            tmp[i-1] += dp[i]
        if 0<= i+1 <= 9:
            tmp[i+1] += dp[i]
    dp = copy.deepcopy(tmp)


print(sum(dp))
