def solution(players, m, k):
    n = len(players)
    dp = [0] * n
    cnt = 0
    
    for i in range(n):
        if players[i] >= m:
            needed = players[i] // m
            plus = needed - dp[i]
            if plus > 0 :
                cnt += plus
                for j in range(k): #k시간 동안 서버 유지
                    if i + j < n:
                        dp[i+j] += plus
            
    return cnt